'''
This route handles the requests send by retrobiocat and distributes it
'''


from flask_restx import Resource, Namespace, Model, fields

from Models.retrobiocat_query_payload import PayloadRetrobiocat
from retrobiohub.retrobiocat_biocathub_mapper.retrobiocat_biocathub_mapper import RetrobiocatBiocathubMapper
from Models.parser_for_planning import Retrobiocat_model as rbc_model


ns = Namespace("Request Handler", description="Routes handling Requests from Retrobiocat")


modelExperiment = PayloadRetrobiocat().define_reaction()

model = ns.model("Experiment", modelExperiment)


class RequestHandler(Resource):
    '''
    Test Instance this class will be removed in the near future
    '''
    @ns.doc(body=model, model=model)
    def post(self):

        new = RetrobiocatBiocathubMapper(rbc_model)
        payload = new.map_reactions_to_enzymes()

    
        return payload

class ResponseHeader(Resource):
    '''
    Test Instance this class will be removed in the near future
    '''
    @ns.doc(body=model)
    def get(self):
        return "444"


ns.add_resource(RequestHandler, "/retrobiocat")
ns.add_resource(ResponseHeader, "/res")

