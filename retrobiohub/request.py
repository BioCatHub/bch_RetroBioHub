'''
This route handles the requests send by retrobiocat and distributes it
'''


from flask_restx import Resource, Namespace, Model, fields
from flask import request


import json

from Models.retrobiocat_query_payload import PayloadRetrobiocat
from retrobiohub.retrobiocat_biocathub_mapper.retrobiocat_biocathub_mapper import RetrobiocatBiocathubMapper
#from Models.parser_for_planning import Retrobiocat_model as rbc_model
import retrobiohub.mini_mongo_adapter as MiniMongo 


ns = Namespace("Request Handler", description="Routes handling Requests from Retrobiocat")


modelExperiment = PayloadRetrobiocat().define_reaction()

model = ns.model("Experiment", modelExperiment)


class RequestHandler(Resource):
    '''
    Test Instance this class will be removed in the near future
    '''
    @ns.doc(body=model, model=model)
    def post(self):

        rbc_model = request.get_json()
        new = RetrobiocatBiocathubMapper(rbc_model)
        
        payload = new.map_reactions_to_enzymes()

        db = MiniMongo.MiniMongo()
        
        
        #db.get_collection()
        id = db.push_document(payload)
        print("die id ist:", id)
        res = json.dumps({"payload":payload, "id":str(id)})
        return res

ns.add_resource(RequestHandler, "/")

