from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional
from datetime import datetime
import models, schemas
from database import get_db

router = APIRouter(prefix="/api/tickets", tags=["tickets"])

def generate_ticket_id(db: Session):
    count = db.query(models.Ticket).count()
    return f"TKT-{str(count + 1).zfill(3)}"

@router.post("", response_model=dict)
def create_ticket(ticket: schemas.TicketCreate, db: Session = Depends(get_db)):
    ticket_id = generate_ticket_id(db)
    db_ticket = models.Ticket(**ticket.dict(), ticket_id=ticket_id)
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return {"ticket_id": db_ticket.ticket_id, "created_at": db_ticket.created_at}

@router.get("")
def list_tickets(
    status: Optional[str] = Query(None),
    search: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(models.Ticket)
    if status:
        query = query.filter(models.Ticket.status == status)
    if search:
        like = f"%{search}%"
        query = query.filter(
            models.Ticket.customer_name.like(like) |
            models.Ticket.customer_email.like(like) |
            models.Ticket.ticket_id.like(like) |
            models.Ticket.description.like(like)
        )
    tickets = query.order_by(models.Ticket.created_at.desc()).all()
    return tickets

@router.get("/{ticket_id}", response_model=schemas.TicketOut)
def get_ticket(ticket_id: str, db: Session = Depends(get_db)):
    ticket = db.query(models.Ticket).filter(models.Ticket.ticket_id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket

@router.put("/{ticket_id}")
def update_ticket(ticket_id: str, update: schemas.TicketUpdate, db: Session = Depends(get_db)):
    ticket = db.query(models.Ticket).filter(models.Ticket.ticket_id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    if update.status:
        ticket.status = update.status
    ticket.updated_at = datetime.utcnow()
    if update.note:
        note = models.Note(ticket_id=ticket_id, note_text=update.note)
        db.add(note)
    db.commit()
    db.refresh(ticket)
    return {"success": True, "updated_at": ticket.updated_at}