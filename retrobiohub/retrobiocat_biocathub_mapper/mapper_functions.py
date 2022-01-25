
from Models.biocathub_model_pydantic import Reactant, Reactantcls, Reaction, Reactioncls
from retrobiohub.pubchem_adapter.pubchem_adapter import PubchemAdapter


class ReactionMapper:
    def __init__(self, rbc_model):
        self.rbc_model = rbc_model
    
    
    def query_iupac_by_smiles(self, smiles):
        '''
            Serves as adapter between the mapper methods and the pubchem adapter. 
            It gets the smiles code as argument, passes it to the Pubchem adapter object and returns the IUPAC name
            ----------
            args:
                smiles: String; SMILES code of the Reagent of interest
            ----------
            returns: 
                iupac: String; IUPAC name of the in the argument submitted SMILES code
            
        '''

        return PubchemAdapter().get_IUPAC_form_smiles(smiles)
        
    
    
    def map_reactants(self):

        educts_list = []
        for i in self.rbc_model["substrates"]:
            iupac = self.query_iupac_by_smiles(i)
            new = Reactant.from_orm(Reactantcls("substrate", i, iupac))
            educts_list.append(new)
            return educts_list
        
        print("educts_list:",educts_list)

    
    def map_products(self):

        products_list = []
        for i in self.rbc_model["products"]: #TODO #11
            iupac = self.query_iupac_by_smiles(i)
            new = Reactant.from_orm(Reactantcls("product", i, iupac))
            products_list.append(new)
        return products_list

    def map_reaction(self):
        reaction_list = []
        new = Reaction.from_orm(Reactioncls(self.rbc_model["reaction"],self.map_reactants(), self.map_products()))
        reaction_list.append(new)
        return(new)


