import asyncio
from datetime import datetime, timedelta
from decimal import Decimal
from uuid import uuid4

from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.config import Settings
from app.models.inv import InvoiceDB, InvoiceItemDB

settings = Settings()

engine = create_async_engine(
    settings.DATABASE_URL,
    echo=False,
    pool_size=settings.DB_POOL_SIZE,
    max_overflow=settings.DB_MAX_OVERFLOW,
)

AsyncSessionLocal = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

ITEM_CATALOG = [
    ("Web development services", Decimal("120.00"), "hours"),
    ("UI/UX design", Decimal("95.00"), "hours"),
    ("Backend API integration", Decimal("110.00"), "hours"),
    ("Cloud infrastructure setup", Decimal("150.00"), "hours"),
    ("Monthly maintenance", Decimal("800.00"), "pcs"),
    ("Consulting", Decimal("200.00"), "hours"),
]


def calculate_item_totals(
    quantity: Decimal,
    unit_price: Decimal,
    tax_rate: Decimal,
    discount_percent: Decimal,
):
    line_total = quantity * unit_price
    discount_amount = line_total * discount_percent / Decimal("100")
    taxable_amount = line_total - discount_amount
    tax_amount = taxable_amount * tax_rate / Decimal("100")
    total_amount = taxable_amount + tax_amount

    return (
        discount_amount,
        taxable_amount,
        tax_amount,
        total_amount,
    )


async def seed():
    async with AsyncSessionLocal() as session:
        for i in range(1, 11):
            issue_date = datetime.utcnow() - timedelta(days=i * 3)
            due_date = issue_date + timedelta(days=30)

            invoice = InvoiceDB(
                invoice_number=f"INV-2025-{1000 + i}",
                issue_date=issue_date,
                due_date=due_date,
                customer=f"Client {i}",
                status="sent",
                notes="Thank you for your business.",
                terms="Net 30",
            )

            session.add(invoice)
            await session.flush()  # ensures invoice.id exists

            subtotal = Decimal("0")
            total_tax = Decimal("0")
            total_discount = Decimal("0")

            items_count = 3 + (i % 4)  # 3–6 items

            for j in range(items_count):
                desc, price, unit = ITEM_CATALOG[(i + j) % len(ITEM_CATALOG)]
                quantity = Decimal(str(1 + (j % 3)))
                tax_rate = Decimal("18")
                discount_percent = Decimal("5") if j % 3 == 0 else Decimal("0")

                (
                    discount_amount,
                    taxable_amount,
                    tax_amount,
                    total_amount,
                ) = calculate_item_totals(
                    quantity, price, tax_rate, discount_percent
                )

                item = InvoiceItemDB(
                    invoice_id=invoice.id,
                    description=desc,
                    quantity=quantity,
                    unit_price=price,
                    unit=unit,
                    tax_rate=tax_rate,
                    discount_percent=discount_percent,
                    discount_amount=discount_amount,
                    taxable_amount=taxable_amount,
                    tax_amount=tax_amount,
                    total_amount=total_amount,
                )

                session.add(item)

                subtotal += quantity * price
                total_discount += discount_amount
                total_tax += tax_amount

            invoice.subtotal = subtotal
            invoice.discount_amount = total_discount
            invoice.tax_amount = total_tax
            invoice.total_amount = subtotal - total_discount + total_tax
            invoice.balance_due = invoice.total_amount

        await session.commit()


if __name__ == "__main__":
    asyncio.run(seed())
