from flask import Flask, request, render_template

app = Flask(__name__)

@app.get("/")
def showhtml():
    return render_template("<h1>This is server HTML</h1>")

if(__name__ == "__main__"):
    app.run()