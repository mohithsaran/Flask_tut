from flask import Flask,render_template,request,url_for,redirect,session

app=Flask(__name__)
#setting a secret key
app.secret_key="hello"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login",methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user=request.form['name']
        # assigning user to session dictionary
        session['user']=user 
        return redirect(url_for('user',user=user))
    else:   
        if "user" in session:
            return redirect(url_for("user",user=session['user'])) 
        return render_template("login.html")

@app.route("/<user>")
def user(user):
    if "user" in session:
        # fetching user from session and assigning to usr variable
        user=session['user']
        return f"<h1>{user}</h1>"
    else:
        # if session is completed then redirect to login
        return redirect(url_for('login'))

@app.route('/logout')    
def logout():
    session.pop('user',None)
    return redirect(url_for('login'))

if __name__=="__main__":
    app.run(debug=True)