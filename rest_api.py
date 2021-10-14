from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.secret_key = "someRandomComboOfLettersLol1999"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:FDM_fcg3_2021@localhost/FullStackDev'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(minutes=5)

db = SQLAlchemy(app)


class category(db.Model):
    category_id = db.Column("category_id", db.Integer, unique=True, primary_key=True, nullable=False)
    name = db.Column("name", db.String(80), nullable=False)
    description = db.Column(db.String(120))

    def __init__(self, name):
        self.name = name


class seller(db.Model):
    seller_id = db.Column("seller_id", db.Integer, primary_key=True)
    password = db.Column(db.String(32), nullable=False)
    name = db.Column("name", db.String(32))
    email = db.Column("email", db.String(32))
    bio = db.Column(db.String(256))

    def __init__(self, password, name, email):
        self.password = password
        self.name = name
        self.email = email


class product(db.Model):
    product_id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False)
    userid = db.Column(db.String(20), nullable=False) 
    category = db.Column(db.String(50))
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120))
    price = db.Column(db.String(20), nullable=False)
    colour = db.Column(db.String(20))


class pic(db.Model):
    pic_id = db.Column(db.Integer, unique=True, primary_key=True)
    img = db.Column(db.Text, unique=True,nullable=False)
    name = db.Column(db.Text, nullable=False)
    mimetype = db.Column(db.Text, nullable=False)

    def __init__(self, img, name, mimetype):
        self.img = img
        self.name = name
        self.mimetype = mimetype


@app.route("/")
def index():
    return render_template("index.html")

# @app.route("/<name>")
# def index(name):
#     return render_template("index.html", content=["nat", "kat", "matt"])

@app.route("/view")
def view():
    return render_template("view.html", values=users.query.all())

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user

        found_user = users.query.filter_by(name=user).first()
        if found_user:
            session["email"] = found_user.email
        else:
            usr = users(user, "")
            db.session.add(usr)
            db.session.commit()

        flash("Logged in successfully!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already logged in!")
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/user", methods=["POST", "GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]

        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            found_user = users.query.filter_by(name=user).first()
            found_user.email = email
            db.session.commit()
            flash("Email was saved successfully!")
        else:
            if "email" in session:
                email = session["email"]

        return render_template("user.html", email=email)
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    flash("You have been logged out!", "info")
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for("login"))

@app.route("/admin")
def admin():
    return redirect(url_for("user", name="Admin!"))


# @app.route('/processUserInfo/<string:userInfo>', methods=['POST'])
# def processUserInfo(userInfo):
#     userInfo = json.loads(userInfo)
#     print()
#     print('PRODUCT INFO RECEIVED')
#     print(------------------------)
#     print(f"Product Name: {userInfo['name']}")
#     print(f"Product Description: {userInfo['type']}")
#     print()

#     return 'Info Received Successfully'

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)