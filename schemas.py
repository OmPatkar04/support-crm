from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class NoteOut(BaseModel):
    id: int
    note_text: str
    created_at: datetime
    class Config:
        from_attributes = True

class TicketCreate(BaseModel):
    customer_name: str
    customer_email: str
    subject: str
    description: str

class TicketUpdate(BaseModel):
    status: Optional[str] = None
    note: Optional[str] = None

class TicketOut(BaseModel):
    ticket_id: str
    customer_name: str
    customer_email: str
    subject: str
    description: str
    status: str
    created_at: datetime
    updated_at: datetime
    notes: List[NoteOut] = []
    class Config:
        from_attributes = True