from fastapi import HTTPException
from starlette.status import HTTP_404_NOT_FOUND

from supermarket_service.database import DatabaseSession, models
from supermarket_service.interface.fruits import Fruit


class FruitCrud:
    def __init__(self, db_session: DatabaseSession):
        self.db_session = db_session

    def get_fruit_by_id(self, fruit_id: int) -> models.Fruit:
        fruit = self._fetch_fruit_by_id(fruit_id)
        if not fruit:
            raise FruitTourNotFoundException(detail=f'Fruit with id={fruit_id} does not exist')
        return fruit

    def delete_fruit(self, fruit_id: int):
        fruit = self._fetch_fruit_by_id(fruit_id)
        if not fruit:
            raise FruitTourNotFoundException(detail=f'Fruit with id={fruit_id} does not exist')
        self.db_session.delete(fruit)
        self.db_session.flush()

    def create_fruit(self, fruit: Fruit):
        db_fruit = models.Fruit(
            name=fruit.name, expiry_date=fruit.expiry_date, quality=fruit.quality
        )
        self.db_session.add(db_fruit)
        self.db_session.flush()
        return db_fruit

    def _fetch_fruit_by_id(self, fruit_id) -> models.Fruit:
        return self.db_session.query(models.Fruit).filter(models.Fruit.fruitID == fruit_id).one_or_none()


class FruitTourNotFoundException(HTTPException):
    def __init__(self, detail: str):
        self.status_code = HTTP_404_NOT_FOUND
        self.detail = detail