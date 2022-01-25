import requests

r = requests.get('https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/smiles/NC(O)C(=O)c1ccccc1/json')

#print(r.json())

payload = r.json()

namespace = payload["PC_Compounds"]

for i in namespace:
    extractor = i["props"]
    for j in extractor:
        #print(j["urn"])
        label = j["urn"]
        if label["label"] == "IUPAC Name":
            print (j["value"]["sval"])

#print(namespace)