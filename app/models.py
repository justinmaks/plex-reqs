from . import db

class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    type = db.Column(db.String(50), nullable=False)  # 'movie' or 'tv'
    tmdb_id = db.Column(db.Integer, nullable=False)
    poster_path = db.Column(db.String(200), nullable=True)  # New field for poster path