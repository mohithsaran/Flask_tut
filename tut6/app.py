from flask import Flask,render_template,request,url_for,redirect,session,flash
from datetime import timedelta

app=Flask(__name__)
#setting a secret key
app.secret_key="hello"
app.permanent_session_lifetime=timedelta(minutes=2)

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

@app.route("/<user>")
def user(user):
    if "user" in session:
        flash('Login Successful')
        # fetching user from session and assigning to usr variable
        user=session['user']
        return render_template("user.html",user=user)
    else:
        flash("You are not logged in!")
        # if session is completed then redirect to login
        return redirect(url_for('login'))

@app.route('/logout')    
def logout():
    if "user" in session:
        user=session['user']
        flash(f"You have been logged out", "info") #info is optional

    session.pop('user',None)
    return redirect(url_for('login'))

if __name__=="__main__":
    app.run(debug=True)