from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class Reactant(BaseModel):
    name:Optional[str]
    role:str
    smiles:str
    
    class Config:
        orm_mode = True

class Reaction(BaseModel):
    name:str
    educts:Reactant
    products:Reactant
    
    class Config:
        orm_mode= True

class Enzyme(BaseModel):
    name: str
    reactions:Reaction

    class Config:
        orm_mode=True


class Reactantcls:
    def __init__(self, name:str, role:str, smiles:str):
        self.name = name
        self.role = role
        self.smiles = smiles

class Reactioncls:
    def __init__(self, name, educts, products):
        self.name = name
        self.educts = educts
        self.products = products

class Enzymecls:
    def __init__(self, name, reactions):
        self.name = name
        self.reactions = reactions

educts = Reactant.from_orm(Reactantcls(2, "reaktion", "fsfgf"))
products = Reactant.from_orm(Reactantcls("hipp", "Gin", "kisbökg"))

reaction = Reaction.from_orm(Reactioncls("reaktiones", educts, products))

enzyme = Enzyme.from_orm(Enzymecls("aaaaase", reaction))

print(enzyme.dict())

newReac = Reactant(role="aesfr", smiles="dsfd")




