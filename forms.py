from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,TextAreaField,SelectMultipleField
from wtforms.validators import DataRequired,Length,Email,EqualTo

class ContactForm(FlaskForm):
    firstname = StringField('firstname')
    
    lastname = StringField('lastname')
    
    email = StringField('email')
    
    number = StringField('number')
    
    residence = StringField('residence')
    
    # reason = SelectMultipleField('reason', choices=["Make an enquiry","Give feedback and suggestions","Request for business and meeting information","Give compliments","Submit a complaint"],validate_choice=False)
    
    reason = StringField('reason', render_kw={"placeholder": "I would like to:"})
    
    message = TextAreaField('message')
    
    submit = SubmitField('Submit')