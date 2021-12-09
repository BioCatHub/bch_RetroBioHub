from flask import Flask
from flask_restx import Resource, Api


from retrobiohub.request import ns  

app = Flask(__name__)
api = Api(app, title="RetroBioHub Microservice")

api.add_namespace(ns, "/request")

if __name__ == "__main__":
    app.run(debug=True) #

