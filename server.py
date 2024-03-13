from flask import Flask
from flask import request
import json
from config import db

products = []

app = Flask(__name__)

@app.get("/")
def home():
    return "Hello from flask"

@app.get("/testing")
def test():
    return "Hello from another page"

@app.get("/about")
def about():
    me = {"name":"Rami"}
    return json.dumps(me)

@app.get("/version")
def version():
    version = {"name": "mouse","version":"2","build":123456}
    return json.dumps(version)

@app.get("/blog")
def blog():
    return "Blog page"

#read and write into the server

@app.get("/api/products")
def get_products():
    return json.dumps(products)

@app.post("/api/products")
def save_products():
    #should save a new product
    product = request.get_json()
    #print(product)
    #mock the save
    #products.append(product)
    #db.products.insert_one(product)
    products.append(product)
    
    return json.dumps(products)






app.run(debug=True)#apply the changes on the code live 

#API/ Endpoint

#Transform JSON/ convert JSON into object again
