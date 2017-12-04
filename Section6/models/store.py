from db import db


class StoreModel(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    items = db.relationship("ItemModel", lazy="dynamic")  # lazy=dynamic delays items list creation until usage.  It turns items from a list into a query.

    def __init__(self, name):
        self.name = name

    def json(self):
        return {"name": self.name, "items": [x.json() for x in self.items.all()]}  # must be self.items.all() because items is now a query if lazy=dyanmic in relationship above

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):    # formerly "insert"
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):    # formerly "update"
        db.session.delete(self)
        db.session.commit()

