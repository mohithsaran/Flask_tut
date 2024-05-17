from flask import Flask, render_template, request, url_for, redirect, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Setting a secret key
app.secret_key = "hello"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(minutes=2)

db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    
    def __init__(self, name, email):
        self.name = name
        self.email = email

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/view")
def view():
    return render_template("view.html", values=users.query.all())


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.permanent = True
        user = request.form['name']
        # Assigning user to session dictionary
        session['user'] = user 
        found_user = users.query.filter_by(name=user).first()
        if found_user:
            session['email'] = found_user.email
        else:
            #user doesnt exist then create user
            usr = users(user, "")
            db.session.add(usr)
            db.session.commit()
        flash('Login Successful')
        return redirect(url_for('user', user=user))
    else:   
        if "user" in session:
            flash("Already logged in")
            return redirect(url_for("user", user=session['user'])) 
        return render_template("login.html")

@app.route("/<user>", methods=["POST", "GET"])
def user(user):
    if "user" in session:
        user = session['user']
        if request.method == "POST":
            email = request.form['email']
            session['email'] = email
            found_user = users.query.filter_by(name=user).first()
            found_user.email = email
            db.session.commit()
            flash('Email was saved')
        else:
            if "email" in session:
                email = session['email']
        return render_template("user.html", user=user)
    else:
        flash("You are not logged in!")
        return redirect(url_for('login'))

@app.route('/logout')    
def logout():
    flash("You have been logged out", "info")  # info is optional
    session.pop('user', None)
    session.pop('email', None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
