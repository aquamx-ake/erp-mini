
from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from database import get_session
from models import Product

router = APIRouter(prefix="/products")

@router.post("/")
def create_product(product: Product, session: Session = Depends(get_session)):
    session.add(product)
    session.commit()
    session.refresh(product)
    return product

@router.get("/")
def list_products(session: Session = Depends(get_session)):
    return session.exec(select(Product)).all()
