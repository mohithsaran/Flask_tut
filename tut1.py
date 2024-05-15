from flask import Flask

#Flask constructor takes the name of current module
app=Flask(__name__)

#route function of the flask class
#which tells the app which URL to call
#Default - GET request
@app.route("/")
def home():
    return "Hello World <h1>Hello</h1>"

@app.route('/hello/<name>')
def user(name):
    return f"Hello {name}"

#main driver function
if __name__=="__main__":
    #to run the flask application on local server 5000 port
    app.run()