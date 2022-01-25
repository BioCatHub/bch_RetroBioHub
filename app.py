'''
Entrypoint to the Retrobiohub Package. In this module the python flask app is instanciated.
'''

from flask import Flask
from flask_restx import Resource, Api
from flask_cors import CORS


from retrobiohub.request import ns  
from retrobiohub.mini_mongo_query import ns as mini_mongo_query

app = Flask(__name__)
api = Api(app, title="RetroBioHub Microservice")
CORS(app,resources={r'/*':{'origins': '*'}} )


api.add_namespace(ns, "/retrobiohub")
api.add_namespace(mini_mongo_query, "/retrobiohub/minimongo")

if __name__ == "__main__":
    app.run(debug=True) #

