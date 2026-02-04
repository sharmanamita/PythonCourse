from flask import Flask

app = Flask(__name__)

@app.route("/")
def Hello():
    return "Hello World"

if __name__ ==  "main":
    app.run(debug=True)