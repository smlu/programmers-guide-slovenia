import sys
import requests
from bs4 import BeautifulSoup
import facebook_login

print("Lets get this party started\n")

facebook_username = sys.argv[1:]
facebook_password = sys.argv[2:]
facebook_post_url = sys.argv[3:]
output_html_location_file = sys.argv[4:]

# Get the Facebook session after the login
session = facebook_login.login_into_facebook(facebook_username, facebook_password)

# After obtaining the session, use the Facebook post url from command line arguments to get the HTML
response = requests.get(facebook_post_url)

print(response.content)


# TODO: Extract the post HTML

# TODO: Save the extracted HTML to its own file
