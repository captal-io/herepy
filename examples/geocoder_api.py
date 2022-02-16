#!/usr/bin/env python

from herepy import GeocoderApi

geocoder_api = GeocoderApi(api_key="")

# geocodes given search text
response = geocoder_api.free_form("casa verde, sao paulo - sp, 02546-000, brazil")
print(response.as_dict())

# geocodes given search text with in given boundingbox
response = geocoder_api.address_with_boundingbox(
    searchtext="200 S Mathilda Sunnyvale CA",
    top_left=[42.3952, -71.1056],
    bottom_right=[42.3312, -71.0228],
)
print(response.as_dict())

# geocodes with given address details
response = geocoder_api.address_with_details(
    state="Sao Paulo", district="brooklin", city="Sao Paulo", country="Brazil"
)
print(response.as_dict())

# geocodes with given street and city
response = geocoder_api.street_intersection(street="Barbaros", city="Istanbul")
print(response.as_dict())
