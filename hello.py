from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def index():
    favpizza = ["cheese", "meat", "lettuce"]
    return render_template("index.html", favpizza=favpizza)
   # return "<h1>Hello World</h1>"


@app.route('/user/<name>')

def user(name):
    return render_template("user.html", user_name=name)
    #return "<h1>Hello, {}</h1>".format(name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500