from requests import get
from pprint import PrettyPrinter

BASE_URL = "http://gleague.nba.com"
ALL_JSON = "/prod/v1/today/json"

response = get(BASE_URL + ALL_JSON).json()
print(response)