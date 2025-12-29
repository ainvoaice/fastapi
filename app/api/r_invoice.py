# app/api/routes/invoices.py
from fastapi import APIRouter, Depends, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.db_async import get_db
from app.db.models.model_inv import Invoice, InvoiceItem
from app.schemas.schema_invoice import InvoiceCreate, InvoiceOut
from app.celery.celery_task import create_invoice_embedding

invRou = APIRouter()

@invRou.get("/invoice_list")
async def list_invoices(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Invoice))
    return result.scalars().all()





@invRou.post(    "/create_new_invoice",    response_model=InvoiceOut,    status_code=status.HTTP_201_CREATED)
async def create_invoice(    payload: InvoiceCreate,    db: AsyncSession = Depends(get_db),):
    total_amount = sum(
        i.quantity * i.unit_price for i in payload.items
    )

    invoice = Invoice(
        invoice_number=payload.invoice_number,
        customer_name=payload.customer_name,
        total_amount=total_amount,
        items_map=[
            InvoiceItem(
                description=i.description,
                quantity=i.quantity,
                unit_price=i.unit_price,
            )
            for i in payload.items
        ],
    )

    db.add(invoice)
    await db.commit()
    await db.refresh(invoice)

    # 🚀 fire-and-forget celery task
    create_invoice_embedding.delay(str(invoice.id)) # type: ignore
    
    return invoice
