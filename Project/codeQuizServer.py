from flask import Flask, request, jsonify
from dataprocessService import login, secret_key, questions

app = Flask(__name__)
app.secret_key = secret_key

@app.route('/api/validate-user', methods=['POST'])
def verifyLogin():
    payload = request.get_json()

    username = payload.get('username')
    password = payload.get('password')

    response = login(username, password)

    if response['status'] == 'error':
        return jsonify(response), 401
    else:
        return jsonify(response)
    
@app.get('/api/questions')
def getQuestions():
    token = request.headers.get("Authorization")
    limit = int(request.args.get("limit"))

    print("::token/limit from UI =>", token, limit)
    rsp = questions(token, limit)

    if rsp['status'] == "error":
        return jsonify(rsp), 403
    else:
        return jsonify(rsp)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

if(__name__ == "__main__"):
    app.run()