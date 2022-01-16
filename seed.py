from app import app
from models import db, Pet

db.drop_all()
db.create_all()

p1 = Pet(name="doggy", species="dog", age=1, notes="small good doy", photo_url="https://www.humanesociety.org/sites/default/files/styles/2000x850/public/2020-07/dog-509745.jpg?h=e22bf01e&itok=uN5v47ua")
p2 = Pet(name="Lovedoggy", species="dog", age=1, notes="small good doy", photo_url="https://www.humanesociety.org/sites/default/files/styles/2000x850/public/2020-07/dog-509745.jpg?h=e22bf01e&itok=uN5v47ua")
p3 = Pet(name="Kitty", species="Cat", age=1, notes="small good cat", photo_url="https://www.humanesociety.org/sites/default/files/styles/2000x850/public/2020-07/dog-509745.jpg?h=e22bf01e&itok=uN5v47ua")


db.session.add_all([p1,p2,p3])
db.session.commit()
