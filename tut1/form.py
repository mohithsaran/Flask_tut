from flask import Flask,redirect,url_for,request

app = Flask(__name__)

@app.route("/<user>")
def success(user):
    return f"Welcome {user}"

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user=request.form['name']
        return redirect(url_for('success',user=user))
    else:
        user=request.args.get('name')
        return redirect(url_for('success',user=user))


if __name__ == "__main__":
    app.run()