from flask import Flask, render_template, url_for, flash, redirect
from forms import ContactForm
from flask_sqlalchemy import SQLAlchemy
# from models import Contact

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db=SQLAlchemy(app) 

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(20),  nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    number = db.Column(db.Integer, unique=True ,nullable=False)
    residence = db.Column(db.String(20), nullable=False)
    reason = db.Column(db.String(30), nullable=False)
    message = db.Column(db.String(200))

    def __repr__(self):
        return f"Contact('{self.firstname}','{self.lastname}', '{self.email}','{self.number}','{self.residence}','{self.reason}','{self.message}')"

@app.before_first_request
def create_tables():
    db.create_all()
    

@app.route("/")
@app.route("/home")
def home():
    return render_template('project.html')

@app.route("/aboutus")
def about():
    return render_template('aboutus.html')

@app.route("/booknow")
def book_now():
    return render_template('booknow.html')

@app.route("/contact", methods=['GET','POST'])
def contact():
    form = ContactForm()
    entry=["Make an enquiry","Give feedback and suggestions","Request for business and meeting information","Give compliments","Submit a complaint"]
    if form.is_submitted():
        contact = Contact(firstname=form.firstname.data, lastname=form.lastname.data, email=form.email.data, number=form.number.data, residence=form.residence.data, reason=form.reason.data, message=form.message.data)
        db.session.add(contact)
        db.session.commit()
        print(Contact.query.all())
        return redirect(url_for('home'))
    return render_template('contact.html', form=form,entry=entry)

@app.route("/deals")
def deals():
    return render_template('deals.html')

@app.route("/gallery")
def gallery():
    return render_template('gallery.html')

@app.route("/visa")
def visa():
    return render_template('visa.html')


if __name__ == '__main__':
    app.run(debug=True)

