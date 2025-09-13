from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def f1():
    return "Hello"

@app.route('/get')
def f2():
    d1 = request.args.get('data1')
    d2 = request.args.get('data2')
    return "This is your data"+ d1 + d2

@app.route('/get2/<yourname>/<surname>')
def f3(yourname, surname):
    return "This is your name "+yourname+surname


if __name__ == "__main__":
    app.run()