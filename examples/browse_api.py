#!/usr/bin/env python

from herepy import BrowseApi
from pprint import *

browse_api = BrowseApi(api_key="")

# fetches a list of browse based on a query string
response = browse_api.search(
    coordinates=[-25.444543, -49.258259]
)
print(response.as_dict())

# fetches a list of browse based on a query string and country code
response = browse_api.search_in_country(
    coordinates=[-25.444543, -49.258259], country_code="BRA"
)
print(response.as_dict())

# a list of popular browse around a location
response = browse_api.places_in_circle(
    coordinates=[-25.444543, -49.258259], radius=1000, limit=10
)
pprint(response.as_dict())
