from app import db
from sqlalchemy.dialects.postgresql import JSONB, BIGINT
from datetime import datetime


class SportsDataIO_NBAPlayer(db.Model):
    __tablename__ = 'sports_data_io_nba_player'
    id = db.Column(BIGINT, primary_key=True)
    raw_json = db.Column(JSONB)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


class NBAPlayer(db.Model):
    __tablename__ = 'nba_player'
    player_id = db.Column(BIGINT, primary_key=True)
    team_id = db.Column(BIGINT)
    jersey_number = db.Column(db.Integer)
    position = db.Column(db.String)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    is_valid_to = db.Column(db.DateTime, nullable=False)
    is_latest = True


class SportsDataIO_NBATeam(db.Model):
    __tablename__ = 'sports_data_io_nba_team'
    id = db.Column(BIGINT, primary_key=True)
    raw_json = db.Column(JSONB)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


class SportsDataIO_NBAStadium(db.Model):
    __tablename__ = 'sports_data_io_nba_stadium'
    id = db.Column(BIGINT, primary_key=True)
    raw_json = db.Column(JSONB)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
