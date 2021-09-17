import requests
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")


AUTH_URL = 'https://accounts.spotify.com/api/token'

# POST
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
    
})

# convert the response to JSON
auth_response_data = auth_response.json()

# save the access token
print(auth_response_data)
access_token = auth_response_data['access_token']

headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}
# base URL of all Spotify API endpoints
BASE_URL = 'https://api.spotify.com/v1/browse/new-releases'


# actual GET request with proper header


r = requests.get(BASE_URL,headers=headers)
r = r.json()

for i in range(10):
    print(r ["albums"]["items"][i]["name"])                




