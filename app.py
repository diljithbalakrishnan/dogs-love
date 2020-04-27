# Sri muniappan thunai
from flask import Flask

app = Flask(__name__)             



@app.route("/")                   # at the end point /
def hello():                      # call method hello
    return "Parassini kadavu Muthappa kathalone"         # which returns "hello world"



if __name__ == "__main__": 
    Schema()       # on running python app.py
    app.run(debug=True)                     # run the flask app
