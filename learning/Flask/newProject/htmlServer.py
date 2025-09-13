from flask import Flask, request, render_template, session
from DBConnect.crud import getLoginByUnameAndPwd, setcommit, mycommit, read, getDataById
import sys
sys.path.append("../..")
import json
app = Flask(__name__)
app.secret_key = 'key'

@app.get("/")
def showhtml():
    # return "<h1>This is server HTML</h1>"
    return render_template("first.html")

@app.get("/login")
def login():
    return render_template("login.html")

@app.get("/details")
def details():
    return render_template("details.html")

@app.get("/reg")
def reg():
    return render_template("registration.html")

@app.post("/verify")
def verify():
    formData = request.form
    uname = formData.get('uname')
    password = formData.get('pass')
    
    setcommit(True)
    data = getLoginByUnameAndPwd(uname, password)
    if(data):
        session["userinfo"] = data
        return render_template('first.html')
        # return render_template('first.html', username=f"{data[3]} {data[2]}")
    else:
        return render_template('login.html', error="Invalid credentails!!")

@app.get("/run") 
def WebApp():
    return render_template("index.html")

@app.route("/shop")
def shop():
    if "mylist" in session:
        itemlist=session["mylist"]
    else:
        itemlist=[]
    item = request.args.get("item")
    if item is not None:
        itemlist.append(item)
    
    session["mylist"]=itemlist
    return render_template("shop.html",mylist=session["mylist"])


@app.get("/list")
def getList():
    arr = ["cd", "newspaper", "mouse", "headphones", "keyboard"]
    return render_template("first.html", productList=arr)

@app.post('/api/login')
def getlogin():
    jsondata = request.get_json()
    uname = jsondata['uname']
    pwd = jsondata['password']
    print(uname, pwd)
    data = getLoginByUnameAndPwd(uname=uname, pwd=pwd)
    print(json.dumps(data))
    return json.dumps(data)

# @app.after_request
# def after_request(response):
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
#     response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')

if(__name__ == "__main__"):
    app.run()