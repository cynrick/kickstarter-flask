from flask import Flask, render_template
from flask.ext.script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route("/")
def index():
    return render_template("index.html")