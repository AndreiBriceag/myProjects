import requests, time, sys, urllib, json

req = requests.get('https://api.wheretheiss.at/v1/satellites/25544')
if not req.status_code in (200, 202):
    sys.exit(-1)
# Only if the status code was 200 or 202, will this code be executed.
resp = req.json()
iss_latitude = resp['latitude']
iss_longitude = resp['longitude']
iss_altitude = resp['altitude']
iss_velocity = resp['velocity']

url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())

file = open("iss tracker/iss.txt", "w")
file.write(
  "There are currently " + str(result["number"]) +
  " astronauts on the ISS: \n\n")
 
people = result["people"]
for p in people:
    file.write(p['name'] + " - on board" + "\n")

# Data for the ISS position
def get_iss_data():
    iss_api = 'https://api.wheretheiss.at/v1/satellites/25544'
    request = requests.get(iss_api).json()

    # Print the position and velocity (KM/H, MPH)
    print(f'''
        ---------------------------
        Real-Time ISS Location:
        ---------------------------
        Altitude: {request['altitude']} metres
        Latitude: {request['latitude']}°
        Longitude: {request['longitude']}°
        Velocity (metric): {request['velocity']} km/h
        Velocity (imperial): {request['velocity'] / 1.60934} mph
        ---------------------------
        ''')

# Print the ISS position
def iss_current_data():
    for i in range(1): # for multiple prints
        get_iss_data()
        # time.sleep(5) # for multiple prints


iss_current_data()