import requests


class MiniClient:

    def __init__(self):
        pass

    def fetch_inchi_for_pubchem_cid(self, cids):
        rlist = []
        for cid in cids:
            try:
                print("Requesting %s" % cid)
                url = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/%s/property/InChI/txt' % cid
                response = requests.get(url)
                string = response.content.decode("utf-8")
                rlist.append((cid, string))
            except Exception as e:
                print(e)
                continue
        return rlist




