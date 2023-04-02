from flask import Flask, render_template, url_for, flash, redirect
from forms import ContactForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

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
        print(form.firstname.data)
        print(form.lastname.data)
        print(form.email.data)
        print(form.number.data)
        print(form.residence.data)
        print(form.reason.data)
        print(form.message.data)
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

