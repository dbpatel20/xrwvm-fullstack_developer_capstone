# Uncomment the imports below before you add the function code
# import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")

# def get_request(endpoint, **kwargs):
# Add code for get requests to back end
import requests
import os
from urllib.parse import urlencode

def get_request(endpoint, **kwargs):
    # Build query parameters if any are passed
    params = urlencode(kwargs)  # Automatically handles URL encoding
    
    # Construct the full request URL
    request_url = os.getenv('backend_url') + endpoint
    if params:
        request_url += "?" + params  # Only append `?` if params exist

    print(f"GET from {request_url}")  # Print URL for debugging
    
    try:
        # Send GET request
        response = requests.get(request_url)
        
        # Handle the response based on status code
        if response.status_code == 200:
            return response.json()  # Return the JSON response
        else:
            print(f"Failed with status code {response.status_code}")
            return {"error": "Failed to fetch data"}
    except requests.exceptions.RequestException as e:
        # Catch and log network errors
        print(f"Network exception occurred: {e}")
        return {"error": "Network exception occurred"}


# def analyze_review_sentiments(text):
# request_url = sentiment_analyzer_url+"analyze/"+text
# Add code for retrieving sentiments
def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url+"analyze/"+text
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")

def post_review(data_dict):
    request_url = backend_url+"/insert_review"
    try:
        response = requests.post(request_url,json=data_dict)
        print(response.json())
        return response.json()
    except:
        print("Network exception occurred")