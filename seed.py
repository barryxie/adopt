from app import app
from models import db, Pet

db.drop_all()
db.create_all()

p1 = Pet(name="doggy", species="dog", age=1, notes="small good doy", photo_url="https://www.humanesociety.org/sites/default/files/styles/2000x850/public/2020-07/dog-509745.jpg?h=e22bf01e&itok=uN5v47ua")


db.session.add(p1)
db.session.commit()
