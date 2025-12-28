# app/schemas/invoice.py
from pydantic import BaseModel
from datetime import date
from typing import List, Optional
from uuid import UUID

class InvoiceItemCreate(BaseModel):
    description: str
    quantity: float
    unit_price: float
    
class InvoiceCreate(BaseModel):
    invoice_number: str
    customer_name: str
    items: List[InvoiceItemCreate]


class InvoiceItemOut(BaseModel):
    description: str
    quantity: float
    unit_price: float

    class Config:
        from_attributes = True
        
class InvoiceOut(BaseModel):
    id: UUID
    invoice_number: str
    customer_name: str
    total_amount: float
    items_map: List[InvoiceItemOut]
    
    class Config:
        from_attributes = True


