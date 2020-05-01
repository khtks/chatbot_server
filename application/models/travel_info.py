from application import db


class TravelInfo(db.Model):
    contentID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    addr = db.Column(db.String, nullable=False)
    number = db.Column(db.String, nullable=False)
    img = db.Column(db.String, nullable=False)
    overview = db.Column(db.String, nullable=False)