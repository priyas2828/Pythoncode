import json

# To pass the below string in to the JSON format, we need a module with JSON and import json


odics = '{"K1":"Val1", "K2":"Val2"}'  # Dictionary contains key value pair and it forms as string

# The  result we are gonna store it in json result
json_result = json.loads(odics)  # loads methods will take the string in to json format
print(json_result)
