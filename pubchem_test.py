import pubchempy as pcp
import urllib


#p = pcp.get_properties('IsomericSMILES', 'CC', searchtype='superstructure')


try:

    p = pcp.get_compounds('CCC', 'smiles')

    for i in p:
        #print(i.iupac_name)
        #print(i.inchikey)
        
        if i.iupac_name != None and i.iupac_name !="" and isinstance(i.iupac_name, str):
            print("i is numer:", p.index(i))
            print(i.iupac_name)
            break
            
        else:
            print("i is numer:", p.index(i))
            print("Smiles code not found")

except pcp.BadRequestError as err:
    print("substance not known")




