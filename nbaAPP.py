from __future__ import print_function
from bstScrapper import main
import yaml
from calc import calculadora

from flask import Flask, render_template, request
import os, optparse

app = Flask(__name__)

developer = os.getenv("DEVELOPER", "Fabricio Juarez & Steven Wilson")
environment =  os.getenv("ENVIRONMENT", "Development")

minsAndMax, year, df,data = main("2020") 

@app.route("/")
def home():
    return render_template("home.html", year = year, developer = developer)

@app.route("/dataSearch")
def dataSearch():
    return render_template("dataSearch.html", year = year, minsAndMax = minsAndMax, df = df )

@app.route("/statistics")
def statistics():
    season = request.args.get('season')
    tipo= request.args.get('tipo')
    measure = request.args.get('measure')
    minsAndMax, year, df , data= main(season) 
    sdata = data[tipo]
    return calculadora(measure,sdata)

if __name__ == "__main__":

    debug = False

    if environment == "Development" or environment == "local":
        debug = True
    app.run(host = "127.0.0.1", debug = debug)