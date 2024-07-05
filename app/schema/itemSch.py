from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str
    description: str
    price: int
    on_offer: int

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int

    class Config:
        from_attributes = True
