from __future__ import print_function
from scrapper import teams
import yaml

from flask import Flask, render_template, request
import os, optparse

app = Flask(__name__)

developer = os.getenv("DEVELOPER", "Fabricio Juarez & Steven Wilson")
environment =  os.getenv("ENVIRONMENT", "Development")

@app.route("/")
def home():
    foo = "bar"
    return render_template("home.html", mivariable = foo, developer = developer)

@app.route("/dataSearch")
def dataSearch():
    return render_template("dataSearch.html", teams = teams)

if __name__ == "__main__":

    debug = False

    if environment == "Development" or environment == "local":
        debug = True
    app.run(host = "127.0.0.1", debug = debug)