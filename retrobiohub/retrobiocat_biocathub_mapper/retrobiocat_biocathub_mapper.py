from Models.parser_for_planning import Retrobiocat_model as rbc_model
from Models.biocathub_model_pydantic import Enzyme, Enzymecls
from retrobiohub.retrobiocat_biocathub_mapper.mapper_functions import ReactionMapper



class RetrobiocatBiocathubMapper:
    
    '''
        Class which triggers the mapping process from the Retrobiocat Model to the BioCatHub model.
        ----------
        attr:
        rbc_model: List Retrobiocat Model
        ----------
        returns:

    '''
    
    def __init__(self, rbc_model):
        self.rbc_model = rbc_model

    def map_reactions_to_enzymes(self):
        
        reactions = ReactionMapper(self.rbc_model).map_reaction()
        enzyme = Enzyme.from_orm(Enzymecls(self.rbc_model["enzyme"], reactions))
        

        return enzyme.dict()
        

    

    



    