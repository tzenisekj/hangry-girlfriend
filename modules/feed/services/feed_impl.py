from typing import List
from xmlrpc.client import Boolean
from modules.models.feedings import Feedings
from modules.repository.feeding_repository_impl import FeedingRepositoryImpl
from modules.exceptions.negative_food_exception import NegativeFoodException

class FeedServiceImpl:

    def __init__(self):
        self.repository = FeedingRepositoryImpl()
        pass

    def add(self, Feedings: Feedings) -> Boolean:
        if Feedings.Amount < 0:
            raise NegativeFoodException
        self.repository.add(Feedings)
        return True