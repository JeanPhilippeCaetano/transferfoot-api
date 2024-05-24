from datetime import datetime
from src.Models import db
from src.Models import Team, Player

class Transfer(db.Model):
    __tablename__ = 'transfers'

    transfer_id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    team_id = db.Column(db.BigInteger, db.ForeignKey('teams.team_id'))
    player_id = db.Column(db.BigInteger, db.ForeignKey('players.player_id'))
    transfer_date = db.Column(db.Date, nullable=False)
    amount = db.Column(db.BigInteger, nullable=False)
    created_at = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.Date, nullable=False, default=datetime.utcnow)

    team = db.relationship('Team', back_populates='transfers')
    player = db.relationship('Player', back_populates='transfers')