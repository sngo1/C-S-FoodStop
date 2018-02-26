'''
csFoodStop
Samantha Ngo and Carol Pan
K06 -- Now Put It In Yer Flask
2018-02-27
'''

from flask import Flask, render_template, request

app = Flask("__name__")

list_of_states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
@app.route("/")
def search():
    return render_template("homepage.html", states=list_of_states)



if __name__ == "__main__":
    app.debug = True
    app.run()
