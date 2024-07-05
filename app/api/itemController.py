from fastapi import FastAPI, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from app.db import database
from app.model import itemModel
from app.schema import itemSch

itemModel.Base.metadata.create_all(bind=database.engine)

router = APIRouter()

@router.post("/items/", response_model=itemSch.Item)
def create_item(item: itemSch.ItemCreate, db: Session = Depends(database.get_db)):
    db_item = itemModel.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.get("/items/{item_id}", response_model=itemSch.Item)
def read_item(item_id: int, db: Session = Depends(database.get_db)):
    db_item = db.query(itemModel.Item).filter(itemModel.Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router.put("/items/{item_id}", response_model=itemSch.Item)
def update_item(item_id: int, item: itemSch.ItemCreate, db: Session = Depends(database.get_db)):
    db_item = db.query(itemModel.Item).filter(itemModel.Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    for key, value in item.dict().items():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.delete("/items/{item_id}", response_model=itemSch.Item)
def delete_item(item_id: int, db: Session = Depends(database.get_db)):
    db_item = db.query(itemModel.Item).filter(itemModel.Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return db_item
