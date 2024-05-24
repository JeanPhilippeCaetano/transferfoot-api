from datetime import datetime
from src.Models import db
from src.Models import Team

class Player(db.Model):
    __tablename__ = 'players'

    player_id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    fullname = db.Column(db.String, nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    position = db.Column(db.String, nullable=False)
    value = db.Column(db.BigInteger, nullable=False)
    team_id = db.Column(db.BigInteger, db.ForeignKey('teams.team_id'))
    created_at = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.Date, nullable=False, default=datetime.utcnow)

    team = db.relationship('Team', back_populates='players')
