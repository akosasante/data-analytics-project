from app import api
from sqlalchemy.dialects.postgresql import JSONB
from datetime import datetime

db = api.db

class SportsDataIO_NBAPLayer(db.Model):
    __tablename__ = 'sports_data_io_nba_player'
    id = db.Column(db.BigInteger, primary_key=True)
    raw_json = db.Column(JSONB)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class NBAPlayer(db.Model):
    __tablename__ = 'nba_player'
    player_id = db.Column(db.bigInteger, primary_key=True)
    team_id = db.Column(db.BigInteger)
    jersey_number = db.Column(db.Integer)
    position = db.Column(db.String)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    is_valid_to = db.Column(db.DateTime, nullable=False)
    is_latest = True
