'''
Entrypoint to the Retrobiohub Package. In this module the python flask app is instanciated.
'''

from flask import Flask
from flask_restx import Resource, Api
from flask_cors import CORS


from retrobiohub.request import ns  

app = Flask(__name__)
api = Api(app, title="RetroBioHub Microservice")
CORS(app,resources={r'/*':{'origins': '*'}} )


api.add_namespace(ns, "/")

if __name__ == "__main__":
    app.run() #

