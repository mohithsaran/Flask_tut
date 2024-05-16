from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("square.html")

@app.route("/square/<int:num>",methods=["GET","POST"])
def square(num):
    if request.method == "POST":
        if request.form['num']=='':
            return render_template("square.html")
        elif request.form['num']==None:
            return f"<h1>{num} is not a number</h1>"
        else:
            number=request.form['num']
            square=int(number)*int(number)
            return render_template("answer.html",num=number,squareofnum=square)
        
    if request.method == "GET":
        return render_template("square.html")


if __name__ == "__main__":
    app.run(debug=True)