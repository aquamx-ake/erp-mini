
from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from database import get_session
from models import Customer

router = APIRouter(prefix="/customers")

@router.post("/")
def create_customer(customer: Customer, session: Session = Depends(get_session)):
    session.add(customer)
    session.commit()
    session.refresh(customer)
    return customer

@router.get("/")
def list_customers(session: Session = Depends(get_session)):
    return session.exec(select(Customer)).all()
