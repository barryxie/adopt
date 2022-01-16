from crypt import methods
from flask import Flask, render_template, flash, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from form import PetForm, EditPetForm

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///adopt_pet"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = "thissosecret"
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False



connect_db(app)

@app.route('/')
def home_page():
    """Render home page"""
    pets = Pet.query.all()
    
    return render_template("home.html", pets= pets)

@app.route('/add', methods=["GET", "POST"])
def add_pet():
    form = PetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)

        db.session.add(pet)
        db.session.commit()
        flash(f"Add {pet.name} to the list!")
        return redirect('/')
    else:
        
        return render_template('add_pet_form.html', form=form) 

@app.route('/<int:pet_id>', methods=["GET", "POST"]) 
def show_edit_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm()
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.photo_url.data
        pet.available = form.available.data
        db.session.add(pet)
        db.session.commit()
        flash(f"{pet.name} info has updated")
        return redirect('/')
    else:
        
        return render_template("show_edit.html", pet=pet, form=form)          