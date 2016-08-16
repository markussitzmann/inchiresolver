from hashids import Hashids



from inchi.identifier import InChI, InChIKey
from inchi.models import Inchi

def run():

    inchikey = InChIKey("InChIKey=ASYNRYMUTXBXSQ-WXRBYKJCSA-N")
    print inchikey.element['version']
    print inchikey.element
        
    inchi = Inchi()
    inchi.add_key(inchikey=inchikey)
    
    
    inchi_store = Inchi(block1='BSYNRYMUTXBXSQ', block2='ZXRBYKJCSA', block3='N', version='1')
    inchi_store.save()
    print inchi.id
    print(Inchi.objects.all())
              
        