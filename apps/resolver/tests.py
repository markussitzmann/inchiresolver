from django.test import TestCase

from inchi.identifier import InChIKey
from resolver.models import Inchi


class IdentifierTest(TestCase):
    def setUp(self):
        pass

    def test1(self):
        inchikey = InChIKey("InChIKey=BSYNRYMUTXBXSQ-WXRBYKJCSA-N")
        print(u"Test 1 : %s" % (inchikey.element['version']))
        self.assertEqual(inchikey.element['version'], 1)
        self.assertEqual(inchikey.element['version'], 1)
        
    def test2(self):
        inchikey = InChIKey(block1="BSYNRYMUTXBXSQ", block2="WXRBYKJCSA", block3="N")
        print("Test 2 : %s %s" % (inchikey.element['version'], inchikey))
        print("Test 2 : %s" % repr(inchikey))
        self.assertEqual(inchikey.element['version'], 1)
        self.assertEqual(inchikey.element['well_formatted'], "InChIKey=BSYNRYMUTXBXSQ-WXRBYKJCSA-N")
        self.assertEqual(inchikey.element['well_formatted'], "InChIKey=BSYNRYMUTXBXSQ-WXRBYKJCSA-N")

    def test3(self):
        inchikey = InChIKey(block1="BSYNRYMUTXBXSQ", block2="WXRBYKJCSA", block3="N")
        inchi = Inchi()
        inchi.add_key(inchikey=inchikey)
        inchi.save()
        print(u"Test 3 : %s" % (inchi.id))