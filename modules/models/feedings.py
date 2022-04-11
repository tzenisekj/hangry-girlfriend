from modules.db_model import db
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.sql import func
from typing import Dict

class Feedings(db.Model):
    __tablename__ = "sample"
    Id = db.Column(Integer(), primary_key=True)
    Feeding = db.Column(DateTime(timezone=True), server_default=func.now())
    Amount = db.Column(Integer(), nullable = False)

    def serialize(self) -> Dict:
        vals = self.__dict__
        r_vals = vals.copy()
        for v in vals:
            if v[0] == '_':
                del r_vals[v]
        return r_vals

    def __init__(self, Amount):
        self.Amount = Amount

    def __repr__(self):
        return '<Feeding %r>' % self.Id
