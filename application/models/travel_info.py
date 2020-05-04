from application import db


class TravelInfo(db.Model):
    contentID = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    addr = db.Column(db.String(500), nullable=False)
    phone_number = db.Column(db.String(30), nullable=False)
    img = db.Column(db.String(300), nullable=False)
    overview = db.Column(db.String(2000), nullable=False)

    def __repr__(self):
        return "contentID : %r  /  title : %r  /  addr : %r  /  phone_number : %r  /  img : %r  /  overview : %r" % (self.contentID, self.title, self.addr, self.phone_number, self.img, self.overview)

    def get_title(self):
        return self.title

    def get_addr(self):
        return self.addr

    def get_phone_number(self):
        return self.phone_number

    def get_img(self):
        return self.img

    def get_overview(self):
        return self.overview