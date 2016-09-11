import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))


import requests
from inchi.identifier import InChIKey, InChI
from requests.auth import HTTPBasicAuth


def fetch_inchi_for(id):
    try:
        response1 = requests.get('https://cactus.nci.nih.gov/chemical/structure/NCICADD:CID=%s/stdinchikey' % id)
        inchikey = InChIKey(response1.content)
        response2 = requests.get('https://cactus.nci.nih.gov/chemical/structure/NCICADD:CID=%s/stdinchi' % id)
        inchi = InChI(response2.content)
        return (inchikey, inchi)
    except Exception as e:
        print(e)
        return None


def run():
    for id in range(1,10):
        print(id)
        identifiers = fetch_inchi_for(id)
        print(identifiers)
        if identifiers:
            inchikey, inchistring = identifiers
            print(inchikey)

print(__name__)
if __name__=="__main__":
    run()

#r = requests.get("http://inchiresolver.localhost/")

#o = requests.options("http://inchiresolver.localhost/organizations")

#t = requests.options("http://inchiresolver.localhost/inchis", auth=HTTPBasicAuth('djangoadmin', 'djangoDJANGO'))

#print(t.text)


