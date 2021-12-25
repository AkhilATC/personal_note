from factory import db
from datetime import datetime


class Notes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80),  nullable=False)
    content = db.Column(db.String(300), unique=True, nullable=False)
    time_logged = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return '<User %r>' % self.title