from modules.feed.services.feed import FeedService
import uuid
from modules.models.feedings import Feedings
from modules.db_model import db
from modules.exceptions.negative_food_exception import NegativeFoodException

feed_service = FeedService()
def test_add(app):
    with app.app_context():
        amount = 1
        response = feed_service.add(Feedings(amount))
        assert(response)

def test_add_negative_food(app):
    with app.app_context():
        amount = -1
        try:
            response = feed_service.add(Feedings(amount))
            assert(False)
        except NegativeFoodException as e:
            assert(True)
