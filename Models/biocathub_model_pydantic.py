from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel




# Defining an reactant
class Reactant(BaseModel):
    role:str
    smiles:str
    name:str
    
    class Config:
        orm_mode = True

class Reactantcls:
    def __init__(self, role:str, smiles:str, name:str):
        self.role = role
        self.smiles = smiles
        self.name = name


# Defining the Reaction ****************************************

class Reaction(BaseModel):
    name:str
    educts:List[Reactant]
    products:List[Reactant]

    class Config:
        orm_mode= True

class Reactioncls:
    def __init__(self, name, educts, products):
        self.name = name
        self.educts = educts
        self.products = products
    
    
# Defining the Enzyme**********************************************

class Enzyme(BaseModel):
    name: str
    reaction:Reaction

    class Config:
        orm_mode=True

class Enzymecls:
    def __init__(self, name, reaction):
        self.name = name
        self.reaction = reaction






