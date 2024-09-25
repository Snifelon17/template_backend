from fastapi import APIRouter, Depends

from supermarket_service.database import DatabaseSession
from supermarket_service.database.crud.fruits_crud import FruitCrud
from supermarket_service.interface.fruits import Fruit

router = APIRouter()


@router.get("/{fruit_id}/data")
async def get_data_by_id(fruit_id: int, fruit_crud: FruitCrud = Depends(FruitCrud)):
    return fruit_crud.get_fruit_by_id(fruit_id)

@router.delete("/{fruit_id}/delete", status_code=204)
async def delete_fruit(fruit_id: int, db_session: DatabaseSession, fruit_crud: FruitCrud = Depends(FruitCrud)):
    with db_session.begin():
        fruit_crud.delete_fruit(fruit_id)

@router.post("", status_code=201)
async def create_fruit(
        fruit: Fruit, db_session: DatabaseSession, fruit_crud: FruitCrud = Depends(FruitCrud)
):
    with db_session.begin():
        db_fruit = fruit_crud.create_fruit(fruit)
    db_session.refresh(db_fruit)
    return db_fruit