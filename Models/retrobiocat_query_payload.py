from marshmallow import Schema
from flask_restx import Model, fields

class PayloadRetrobiocat:
    ''' '''

    def define_reaction(self):
        reaction = {
            "reaction":fields.String,
            "enzyme":fields.String,
            "products":fields.List(fields.List(fields.String)),
            "cofactors":fields.List(fields.List(fields.String)),
            "substrates":fields.List(fields.List(fields.String)),
        }
        return reaction