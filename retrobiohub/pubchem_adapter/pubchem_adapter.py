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



    
    def get_IUPAC_form_smiles(self, SMILES):
        '''
            This function is used to query pubchem with a SMILES code and retrieve a IUPAC name
        ----------
        args:
            SMILES: String; the SMILES code of the structure to be queried
        ----------
        return:
            IUPAC: String;  IUPAC name of the structure queried

        '''
        base_smiles = 'compound/smiles/'
        spec_smiles = SMILES
        return_format = '/json'

        query = base_smiles + spec_smiles + return_format
        payload = self.pubchem_connector(query).json()
        namespace = payload["PC_Compounds"]

        for i in namespace:
            extractor = i["props"]
            for j in extractor:
                #print(j["urn"])
                label = j["urn"]
                if label["label"] == "IUPAC Name":
                    iupac = j["value"]["sval"]
                    print (j["value"]["sval"])
                    return iupac
                break
                    

