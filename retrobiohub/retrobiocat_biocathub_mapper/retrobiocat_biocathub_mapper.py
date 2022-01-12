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

        enzymes = []
        for i in self.rbc_model:
            reactions = ReactionMapper(i).map_reaction()
            enzyme = Enzyme.from_orm(Enzymecls(i["enzyme"], reactions))
            enzyme_dict = enzyme.dict()
            enzymes.append(enzyme_dict)
        
        return enzymes
        

    

    



    