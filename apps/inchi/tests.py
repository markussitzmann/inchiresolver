from django.test import TestCase

from inchi.identifier import InChI, InChIKey
from inchi.models import Inchi


class IdentifierTest(TestCase):
    def setUp(self):
        pass

    def test1(self):
        inchikey = InChIKey("InChIKey=BSYNRYMUTXBXSQ-WXRBYKJCSA-N")
        print("Test 1 : %s" % inchikey.version)
        self.assertEqual(inchikey.element['version'], 1)
        self.assertEqual(inchikey.version, 1)
        
    def test2(self):
        inchikey = InChIKey(block1="BSYNRYMUTXBXSQ", block2="WXRBYKJCSA", block3="N")
        print("Test 2 : %s %s" % (inchikey.version, inchikey))
        print("Test 2 : %s" % repr(inchikey))
        self.assertEqual(inchikey.element['version'], 1)
        self.assertEqual(inchikey.element['well_formatted'], "InChIKey=BSYNRYMUTXBXSQ-WXRBYKJCSA-N")
        self.assertEqual(inchikey.well_formatted, "InChIKey=BSYNRYMUTXBXSQ-WXRBYKJCSA-N")