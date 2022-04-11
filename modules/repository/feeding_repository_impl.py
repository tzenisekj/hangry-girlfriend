from typing import List,Dict
from modules.models.feedings import Feedings
from modules.repository.feeding_repository import FeedingRepository
from modules.db_model import db

class FeedingRepositoryImpl(FeedingRepository):

    def __init__(self):
        self.db = db

    def add(self, feeding) -> None:
        db.session.add(feeding)
        db.session.commit()

