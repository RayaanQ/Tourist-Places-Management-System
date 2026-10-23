<div align="center">

# 🗺️ Tourist Places Management System

**A Flask web app for exploring tourist destinations, with a contact form backed by a SQLite database.**

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)

</div>

---

## ✦ Overview

A server-rendered website built with **Flask** and **Flask-SQLAlchemy**. Visitors browse tourist places and send enquiries through a contact form, and each submission is stored in a **SQLite** database through a SQLAlchemy `Contact` model.

## ✦ Getting started

```bash
python -m venv myenv
myenv\Scripts\activate             # macOS/Linux: source myenv/bin/activate
pip install -r requirements.txt
python main.py
```

### Inspect saved enquiries

```python
# in a Python shell from the project folder
from main import app, db, Contact
with app.app_context():
    print(Contact.query.all())
```

---

<div align="center"><sub>Built by <a href="https://github.com/RayaanQ">Rayaan Quraishi</a> · <a href="https://rayaanq.github.io/Portfolio/">Portfolio</a> · <a href="https://www.linkedin.com/in/rayaan-quraishi">LinkedIn</a></sub></div>
