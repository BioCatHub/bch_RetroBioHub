from marshmallow import Schema
from flask_restx import Model, fields
'''

class Products(Schema):
    products = fields.List(fields.Str())

class Substrates(Schema):
    substrates = fields.List(fields.Str())

class Cofactors(Schema):
    cofactors = fields.List(fields.Str())


class Reaction(Schema):
    reaction = fields.Str()
    enzyme = fields.Str()
    products = fields.List(fields.List(fields.Str()))
    cofactors = fields.List(fields.List(fields.Str()))
    substrates = fields.List(fields.List(fields.Str()))

'''
class Experiment:

    def define_reaction(self):
        reaction = {
            "reaction":fields.String,
            "enzyme":fields.String,
            "products":fields.List(fields.List(fields.String)),
            "cofactors":fields.List(fields.List(fields.String)),
            "substrates":fields.List(fields.List(fields.String)),
        }
        return reaction