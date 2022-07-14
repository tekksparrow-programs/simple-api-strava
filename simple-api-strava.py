from requests_oauthlib import OAuth2Session
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Set local id, secret, and redirect_url variables
client_id = os.getenv('STRAVA_CLIENT_ID')
client_secret = os.getenv('STRAVA_CLIENT_SECRET')
redirect_url = "https://tekksparrow-programs.github.io/website/"

# Create session variable
session = OAuth2Session(client_id=client_id, redirect_uri=redirect_url)

# Set auth url and scope variables
auth_base_url = "https://www.strava.com/oauth/authorize"
session.scope = ["profile:read_all"]
auth_link = session.authorization_url(auth_base_url)

# Print auth link and accept input
print(f"Click Here: {auth_link[0]}")
redirect_response = input(f"Paste redirect url here: ")

# Get oauth token
token_url = "https://www.strava.com/api/v3/oauth/token"
token = session.fetch_token(
    token_url=token_url,
    client_id=client_id,
    client_secret=client_secret,
    authorization_response=redirect_response,
    include_client_id=True
)

# Make request to protected resource
response = session.get("https://www.strava.com/api/v3/athlete")

# Print response
print("\n\n\n")
print(f"Response Status: {response.status_code}")
print(f"Response Reason: {response.reason}")
print(f"Time Elaspsed: {response.elapsed}")
print(f"Response Text: \n{'-'*15}\n{response.text}"