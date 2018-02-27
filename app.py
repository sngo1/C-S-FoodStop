'''
csFoodStop
Samantha Ngo and Carol Pan
SoftDev2 pd7
K06 -- Now Put It In Yer Flask
2018-02-27
'''

from flask import Flask, render_template, request
from utils import usreps
import json

app = Flask("__name__")

list_of_states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

@app.route("/")
def options():
    return render_template("homepage.html", states=list_of_states)

@app.route("/find")
def search():
    state = request.args["state"]
    data = json.dumps(usreps.by_state_initials(state))
    print data
    return data


if __name__ == "__main__":
    app.debug = True
    usreps.delete_data()
    usreps.insert_data()
    app.run()
