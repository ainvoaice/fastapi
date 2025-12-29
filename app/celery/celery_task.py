from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from app.db.db_sync import engine_sync
from app.db.models.model_inv import Invoice, InvoiceEmbedding

# example embedding function
def embed_text(text: str) -> list[float]:
    # call OpenAI / local model here
    return [0.0] * 1536


SessionLocal = sessionmaker(bind=engine_sync)

def build_items_chunk(invoice: Invoice) -> str:
    return "\n".join(
        f"{item.description} | qty:{item.quantity} | price:{item.unit_price}"
        for item in invoice.items_map
    )

def build_overall_chunk(invoice: Invoice) -> str:
    return f"""
Invoice #{invoice.invoice_number}
Customer: {invoice.customer_name}
Total: {invoice.total_amount}

Items:
{build_items_chunk(invoice)}
""".strip()


from app.celery.celery_app import celery_app

@celery_app.task(name="create_invoice_embedding")
def create_invoice_embedding(invoice_id: str) -> None:
    db = SessionLocal()
    try:
        invoice = db.execute(
            select(Invoice).where(Invoice.id == invoice_id)
        ).scalar_one()

        items_chunk = build_items_chunk(invoice)
        overall_chunk = build_overall_chunk(invoice)

        embedding = InvoiceEmbedding(
            invoice_id=invoice.id,
            items_chunk=items_chunk,
            items_embedding=embed_text(items_chunk),
            overall_chunk=overall_chunk,
            overall_embedding=embed_text(overall_chunk),
        )

        db.add(embedding)
        db.commit()

    finally:
        db.close()
