from db import db

class PhotographerModel(db.Model):
    __tablename__ = "photographers"
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(80))
    description = db.Column(db.String)
    speciality = db.Column(db.String)

    def __init__(self,name,description,speciality):
        self.name = name
        self.description = description
        self.speciality = speciality
    def json(self):
        return {"name":self.name,"description":self.description,"speciality":self.speciality}
    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name= name).first()

    def save_to_db(self):
            db.session.add(self)
            db.session.commit()
    def delete_from_db(self):
            db.session.delete(self)
            db.session.commit()