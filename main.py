from flask import Flask, render_template, url_for, flash, redirect

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('project.html')

@app.route("/aboutus")
def aboutus():
    return render_template('aboutus.html')

@app.route("/booknow")
def booknow():
    return render_template('booknow.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

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

