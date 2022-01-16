from flask_wtf import FlaskForm
from wtforms import IntegerField,BooleanField,StringField,URLField, SelectField
from wtforms.validators import InputRequired, Optional,URL, NumberRange, Length

class PetForm(FlaskForm):
    name = StringField("Pet name", validators=[InputRequired(message="Pet name can not be blank")])
    species = SelectField("Species",choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")])
    photo_url = URLField("Photo", validators=[URL(), Optional()])
    age = IntegerField("Age",validators=[Optional(), NumberRange(min=0, max=30)])
    notes = StringField("Note", validators=[Optional(), Length(min=10)])

class EditPetForm(FlaskForm):
    
    photo_url = URLField("Photo", validators=[URL(), Optional()])
    notes = StringField("Note", validators=[Optional(), Length(min=10)])
    available = BooleanField("available?")  
    
