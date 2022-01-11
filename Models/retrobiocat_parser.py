
from biocathub_model_pydantic import Reactant, Reactantcls, Reaction, Reactioncls
from parser_for_planning import Retrobiocat_model as RBM

class ReactionMapper:
    def __init__(self, rbc_model):
        self.rbc_model = rbc_model
    
    def map_reactants(self):

        educts_list = []
        for i in self.rbc_model["substrates"]:
            new = Reactant.from_orm(Reactantcls("educt", i))
            educts_list.append(new)
            return educts_list
        
        print("educts_list:",educts_list)

    
    def map_products(self):

        products_list = []
        for i in self.rbc_model["products"]:
            new = Reactant.from_orm(Reactantcls("educt", i))
            products_list.append(new)
        print("educts_list:",products_list)
        return products_list

    def map_reaction(self):
        new = Reaction.from_orm(Reactioncls(self.rbc_model["reaction"],self.map_reactants(), self.map_products()))
        print(new.dict())




new = ReactionMapper(RBM)

#new.map_products()
#new.map_reactants()

new.map_reaction()
