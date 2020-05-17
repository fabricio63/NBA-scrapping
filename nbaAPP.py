from __future__ import print_function
from bstScrapper import main
import yaml
from calc import calculadora
from searching import search
from sorting import sort


from flask import Flask, render_template, request
import os, optparse

app = Flask(__name__)

developer = os.getenv("DEVELOPER", "Fabricio Juarez & Steven Wilson")
environment =  os.getenv("ENVIRONMENT", "Development")

minsAndMax, year, df ,data, sortedTeamsList, sortedWinList, sortedWinLossPCT = main("2020") 

@app.route("/")
def home():
    return render_template("home.html", year = year, developer = developer)

@app.route("/dataPreview")
def dataPreview():
    return render_template("dataPreview.html", year = year, minsAndMax = minsAndMax, sortedTL = sortedTeamsList , sortedWL = sortedWinList, sortedWLPCT = sortedWinLossPCT)

@app.route('/dataPreview', methods=['POST'])
def my_form_post():
    arrayInput = request.form['array']
    item = request.form['item']
    array = data[arrayInput]
    return render_template("dataPreview.html", year = year, minsAndMax = minsAndMax, df = df, sortedTL = sortedTeamsList , sortedWL = sortedWinList, sortedWLPCT = sortedWinLossPCT, search  = search("ALL", array , item))

@app.route("/statistics")
def statistics():
    season = request.args.get('season')
    tipo = request.args.get('tipo')
    measure = request.args.get('measure')
    minsAndMax, year, df , data = main(season) 
    sdata = data[tipo]
    return render_template("dataStatistics.html", year = year, calc = calculadora(measure,sdata))

if __name__ == "__main__":

    debug = False

    if environment == "Development" or environment == "local":
        debug = True
    app.run(host = "127.0.0.1", debug = debug)