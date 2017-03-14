import requests

from lib.mini_client import MiniClient

c = MiniClient()
ilist = c.fetch_inchi_for_pubchem_cid(range(1, 100))

data = [{'string': i} for cid, i in ilist]

for cid, i in ilist:
    r = requests.post("http://inchiresolver.localhost/inchis/", data={'string': i},
                      auth=('djangoadmin', 'djangoDJANGO'))

    print(r)
    f = open('out.html', 'w')
    f.write(r.content.decode("utf-8"))
    print('end')