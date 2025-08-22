
from fastapi import APIRouter, Depends
from sqlmodel import Session
from database import get_session
from models import Invoice

router = APIRouter(prefix="/invoices")

@router.post("/")
def create_invoice(invoice: Invoice, session: Session = Depends(get_session)):
    session.add(invoice)
    session.commit()
    session.refresh(invoice)
    return invoice

@router.get("/")
def list_invoices(session: Session = Depends(get_session)):
    return session.exec(session.query(Invoice)).all()
