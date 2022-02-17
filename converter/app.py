from flask import Flask, request, render_template, redirect, url_for, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyRates
from forex_python.converter import CurrencyCodes
from convert import Convert

app = Flask(__name__)

# the toolbar is only enabled in debug mode:
app.debug = True

# set a 'SECRET_KEY' to enable the Flask session cookies
app.config['SECRET_KEY'] = 'choco'

toolbar = DebugToolbarExtension(app)

c = CurrencyRates()
s = CurrencyCodes()
f = Convert()

@app.route("/", methods =["GET", "POST"])
def home():
    if request.method == "POST":
        Currency1 = request.form["Currency1"]
        Currency2 = request.form["Currency2"]
        Amount = request.form["Amount"]
        Converted_Amount = round(c.convert(Currency1, Currency2, int(Amount)), 2)
        symbol = s.get_symbol(Currency2)
        if f.CheckType(int(Amount)):
            return render_template("results.html", Currency1=Currency1, Currency2=Currency2, Amount=Amount, Converted_Amount=Converted_Amount, symbol=symbol )
        else:
            return render_template("index.html")
    else:
        return render_template("index.html")

@app.route("/results")
def results():
    
    return render_template("results.html")

#round the coverted amount to the nearest 10th
# add currency symbol