from flask import Flask,render_template,request,url_for,redirect,session,flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
#setting a secret key
app.secret_key="hello"
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///users.sqlite3' #sqlite:///table.sqlite3
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.permanent_session_lifetime=timedelta(minutes=2)

db=SQLAlchemy(app)

class users(db.Model):
    _id=db.Column("id",db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    email=db.Column(db.String(100))
    
    def __init__(self,name,email):
        self.name=name
        self.email=email


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login",methods=['GET','POST'])
def login():
    if request.method == 'POST':
        session.permanent=True
        user=request.form['name']
        # assigning user to session dictionary
        session['user']=user 
        
        return redirect(url_for('user',user=user))
    else:   
        if "user" in session:
            flash("Already you are logged in")
            return redirect(url_for("user",user=session['user'])) 
        return render_template("login.html")

@app.route("/<user>",methods=["POST","GET"])
def user(user):
    if "user" in session:
        flash('Login Successful')
        user=session['user']
        if request.method=="POST":
            email=request.form['email']
            session['email']=email
        else:
            if "email" in session:
                email=session['email']
        return render_template("user.html",user=user)
    else:
        flash("You are not logged in!")
        # if session is completed then redirect to login
        return redirect(url_for('login'))

@app.route('/logout')    
def logout():
        
    flash(f"You have been logged out", "info") #info is optional
    session.pop('user',None)
    session.pop('email',None)
    return redirect(url_for('login'))

if __name__=="__main__":
    db.create_all()
    app.run(debug=True)