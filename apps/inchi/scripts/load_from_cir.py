from django.db.utils import IntegrityError
import requests

from inchi.identifier import InChIKey, InChI
from inchi.models import Inchi


def fetch_inchi_for(id):
    try:
        response1 = requests.get('http://cactus.nci.nih.gov/chemical/structure/NCICADD:CID=%s/stdinchikey' % id)
        inchikey = InChIKey(response1.content)
        response2 = requests.get('http://cactus.nci.nih.gov/chemical/structure/NCICADD:CID=%s/stdinchi' % id)
        inchi = InChI(response2.content)
        return (inchikey, inchi)
    except:
        return None


def run():
    for id in xrange(1,10000):
        print id
        identifiers = fetch_inchi_for(id)
        print identifiers
        if identifiers:
            inchikey, inchistring = identifiers
            try:
                inchi = Inchi()
                inchi.add_key_and_string(inchikey, inchistring)
            except IntegrityError as e:
                print e
                print "Skipped"
                pass
    
