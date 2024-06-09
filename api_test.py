import requests

# Provided API key and token
api_key = 'xxxxxxxx'
app_token = 'xxxxxxxx'

# Google Maps API request URL
maps_url = f'https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key={api_key}'

# Example request using app token (replace with actual endpoint)
app_token_url = f'https://api.example.com/secure-endpoint?app_token={app_token}'

# Making the requests
maps_response = requests.get(maps_url)
app_token_response = requests.get(app_token_url)

# Printing the responses
print("Google Maps API Response:")
print(maps_response.json())

print("\nApp Token Response:")
print(app_token_response.json())
