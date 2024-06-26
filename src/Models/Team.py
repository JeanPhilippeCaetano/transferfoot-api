from datetime import datetime

from src.Models import db
from src.Models import Player
from src.Models import Transfer


class Team(db.Model):
    __tablename__ = 'teams'

    team_id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    country = db.Column(db.String, nullable=False)
    creation_date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    created_at = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.Date, nullable=False, default=datetime.utcnow)

    players = db.relationship('Player', back_populates='team', lazy='dynamic')
    transfers = db.relationship('Transfer', back_populates='team', lazy='dynamic')