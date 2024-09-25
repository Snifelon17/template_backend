from datetime import date
from pydantic import BaseModel


class Fruit(BaseModel):
    name: str
    expiry_date: date
    quality: int

class FruitRead(Fruit):
    fruitID: int