from flask import Flask
from flask import make_response
import json

app = Flask(__name__)

@app.route("/set_cookie")
def index():
    resp = make_response("success")
    itcast = resp.set

if __name__ == "__main__":
    app.run(debug=True)