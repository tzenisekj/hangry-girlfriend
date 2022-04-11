import datetime, time
from modules.repository.feeding_repository_impl import FeedingRepositoryImpl
from modules.models.feedings import Feedings
from modules.db_model import db

repository = FeedingRepositoryImpl()
def test_add(app):
    with app.app_context():
        now = datetime.datetime.now()
        time.sleep(1)
        amount = 1
        feeding = Feedings(amount)
        repository.add(feeding)
        contained = False
        for d in Feedings.query.all():
            if d.Feeding >= now:
                contained = True
        assert contained