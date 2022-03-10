import datetime

from app import db


class Result(db.Model):
    __tablename__ = 'results'
    Id = db.Column(db.Integer, primary_key=True, nullable=False)
    LoadResult = db.Column(db.String(2048))
    AvgRPS = db.Column(db.Integer)
    CreateDateUtc = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow())

    def __repr__(self):
        return str({k: v for k, v in self.__dict__.items() if k[0].isupper()})
