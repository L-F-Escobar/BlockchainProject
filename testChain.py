import requests

 # URL end point.
url = 'http://localhost:8000/transactions/new'

# HTTP Action.
HTTP_action = 'POST'

# Header Parameters.
headers = {
        'Content-Type' : 'application/json',
        'Cache-Control': 'no-cache'
}

# Dynamically set key/value body pairs. Body code has the ability to
# exclude a key/value pair, set pair to null, or assign values.
body = {'sender':'dsdvsdvsdav',
         'recipient':'sadvasdvsdvsdvsdvsdvsd',
         'amount':5}

# Make HTTPS Request.
response = requests.request(HTTP_action, url, json=body, headers=headers, verify=False)
# responseBody = response.json()

print(response.text)
print(response)
# print(responseBody)