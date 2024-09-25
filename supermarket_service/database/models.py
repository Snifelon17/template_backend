from datetime import date

from sqlalchemy import Column, Integer, String, Date, Sequence
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Fruit(Base):
    __tablename__ = "fruit"

    fruitID: int = Column(Integer, Sequence('fruit_id_seq'), primary_key=True)
    name: str = Column(String, nullable=False)
    expiry_date: date = Column(Date, nullable=False)
    quality: int = Column(Integer)