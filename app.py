# Sri muniappan thunai
from flask import Flask, request, jsonify
from models import Schema
from service import ToDoService
import json

app = Flask(__name__)             




@app.route("/")                   
def hello():                      
    return "Parassini kadavu Muthappa kathalone"  
           

@app.route("/todo", methods=["POST"])
def create_todo():
    return ToDoService().create(request.get_json())



if __name__ == "__main__": 
    Schema()       
    app.run(debug=True, port=5000)       