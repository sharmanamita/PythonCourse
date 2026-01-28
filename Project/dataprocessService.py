from crud import validateUserCredentials, createResponse, getNextQuestion
# import crud
import jwt
from datetime import timedelta, datetime

secret_key = "CodeQuizApp"


def login(uname, pwd):
    token = generateJwtToken(uname)
    data = validateUserCredentials(uname, pwd)

    if data != None:
        return createResponse("sucess", "Login Successfull", {"firstname": data[3], "lastname": data[2]}, token)
    else:
        return createResponse("error", "Invalid username and password", None)
    
def questions(token, limit):
    token = validateJwtToken(token)
    q_generator = questionGen(limit)
    results = []

    while True:
        try:
            row = next(q_generator)
            results.append(row)
        except StopIteration as error:
            break
    
    if token:
        if results != None and len(results) > 0:
            return createResponse("sucess", "Data fetched successfully!", results, token)
        else:
            return createResponse("error", "Not Authorized", None)
    else:
        return createResponse("error", "Authorization token missing!")


def questionGen(limit):
    start = (limit - 10) + 1
    end = limit + 1

    for x in range(start, end):
        yield getNextQuestion(x)
        continue

    
def generateJwtToken(username):
    expiration = datetime.now() + timedelta(hours=1)

    payload = {
        "username": username,
        "exp": expiration
    }

    token = jwt.encode(payload, secret_key, algorithms=["HS256"])

    return token

def validateJwtToken(token):
    token = token.split(" ")[1]
    decodedToken = jwt.decode(token, secret_key, algorithms=["HS256"])
    return decodedToken
    
