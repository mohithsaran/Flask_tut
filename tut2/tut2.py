from flask import Flask,redirect,url_for,render_template

#Flask constructor takes the name of current module
app=Flask(__name__)

#route function of the flask class
#which tells the app which URL to call
#Default - GET request
@app.route("/<name>")
def home(name):
    return  render_template('index.html',content=['Mohith','Saran','Latha','Narasimha','Rao'],row=2)

if __name__=="__main__":
    app.run()