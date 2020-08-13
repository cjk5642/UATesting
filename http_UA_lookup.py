#Script used to test HTTP response headers of a site using multiple UAs
#Currently only top 10 most-used UAs included

#currently hardcoded URL/Domain
import requests
r = requests.get('https://google.com')
r.json()


