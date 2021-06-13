import requests
import json
import jsonpath

api_url = "https://reqres.in/api/users?page=2"

# Make a request and store it in response and retrive the text
response1 = requests.get(api_url)
print(response1.text)
# Validate status code
assert response1.status_code == 200  # the assert statement is used to continue the execute if the given condition
# evaluates to True and it should be success
# If we change it it 201 we should be getting assertion error
# Parse response into JSON format
json_response = json.loads(response1.text)  # Converting response in to json format which the o/p will be {}
print(json_response)
# Apply JSON path
x = jsonpath.jsonpath(json_response, 'total')
print(x[0])
y = jsonpath.jsonpath(json_response, 'data[0].first_name')  # complex json
print(y[0])

# Want to fetch any data in the file or json
for val in json_response['data']:
    print(val['first_name'])