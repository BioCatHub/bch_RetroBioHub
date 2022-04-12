import pubchempy as pcp
import urllib

import requests


class PubchemAdapter:
    '''
        This class is used to query pubchem
    
    '''

    def pubchem_connector(self, query):

        '''
            Builds the Get request needed to query pubchem
        
        '''

        
        base = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/'
        request = requests.get(base+query)

        return request



    
    def get_IUPAC_form_smiles(self, smiles):
        '''
            This function is used to query pubchem via pubchempy with a SMILES code and retrieve a IUPAC name
        ----------
        args:
            SMILES: String; the SMILES code of the structure to be queried
        ----------
        return:
            IUPAC: String;  IUPAC name of the structure queried

        '''
        try:

            p = pcp.get_compounds(smiles, 'smiles')
            for i in p:                
                if i.iupac_name != None and i.iupac_name !="" and isinstance(i.iupac_name, str):
                    return i.iupac_name

                elif i.iupac_name == None:
                    raise
                
                #return i.iupac_name
        except pcp.BadRequestError as err :
            return "Smiles code can't be identified"
        except Exception as err:
            return "Smiles code can't be identified"

                    

