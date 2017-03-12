import json

import requests

from lib.mini_client import MiniClient

auth = ('djangoadmin', 'djangoDJANGO')

nih = {
    'parent': None,
    'name': 'National Institutes of Health',
    'abbreviation': 'NIH',
    'url': 'https://www.nih.gov/'
}


post = requests.post("http://inchiresolver.localhost/organizations/", data=nih, auth=auth)


print(post)
print(post.content)

get = requests.get("http://inchiresolver.localhost/organizations/")

organizations = get.json()
print(organizations)

nci = {
    'parent': 'http://inchiresolver.localhost/organizations/f8b81d4f-24e8-46cc-806c-ad3ff0ba37ec/',
    'name': 'National Cancer Institute',
    'abbreviation': 'NCI',
    'url': 'https://www.cancer.gov/'
}

post = requests.post("http://inchiresolver.localhost/organizations/",
            data=nci,
            auth=('djangoadmin', 'djangoDJANGO'))