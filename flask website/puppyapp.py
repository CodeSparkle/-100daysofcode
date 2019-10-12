from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    name = "Josh"
    food = ["biscuits","milk","cereals"]
    user_logged_in = False
    return render_template("home.html",name = name, food = food, user_logged_in=user_logged_in)

@app.route("/puppy/<name>")
def pupname(name):
    return render_template("name.html",name = name)

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/thankyou")
def thankyou():
    first = request.args.get('first')
    last = request.args.get('last')
    return render_template("thankyou.html", first=first, last=last)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug= True)
