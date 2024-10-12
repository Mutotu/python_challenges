import requests
import geocoder

# List of destinations
destinations = [
    "Space Needle",
    "Crater Lake",
    "Golden Gate Bridge",
    "Yosemite National Park",
    "Las Vegas, Nevada",
    "Grand Canyon National Park",
    "Aspen, Colorado",
    "Mount Rushmore",
    "Yellowstone National Park",
    "Sandpoint, Idaho",
    "Banff National Park",
    "Capilano Suspension Bridge"
]

# Loop through each destination and get the lat-long coordinates
# for destination in destinations:
#     g = geocoder.arcgis(destination)
    # print(f"{destination} is located at {g.latlng}")


# Make sure to replace [YOUR_API_KEY_HERE] with your actual key, which
# will look like a bunch of letters and numbers! Alternatively, copy the sample
# API call from Dark Sky dashboard and just remove the coordinates.
API_BASE_URL = "https://api.darksky.net/forecast/[YOUR_API_KEY_HERE]/"

# Previous code still here.

for destination in destinations:
    g = geocoder.arcgis(destination)
    print(f"{destination} is located at {g.latlng}")

    full_api_url = API_BASE_URL + g.latlng + "," , g.longlng
    result = requests.request('GET', full_api_url).json()

    # From the result, print out the summary and current temperature.