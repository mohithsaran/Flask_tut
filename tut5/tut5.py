from flask import Flask,render_template,request,url_for,redirect,session

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login",methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user=request.form['name']
        session['user']=user
        return redirect(url_for('user'))
    else:    
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    if "user" in session:
        usr=session["user"]
        return f"<h1>{usr}</h1>"
    else:
        return redirect(url_for('login'))

if __name__=="__main__":
    app.run(debug=True)