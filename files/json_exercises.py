# Reading from json
import json

with open('./test_files/purchase_14781239.json') as purchase_json:
  purchase_data = json.load(purchase_json)
 
print(purchase_data['user'])
# Prints 'ellen_greg'

# Writing to json
turn_to_json = {
  "eventId": 674189,
  "dateTime": "2015-02-12T09:23:17.511Z",
  "chocolate": "Semi-sweet Dark",
  "isTomatoAFruit": True,
}

with open('./output_files/output.json', 'w') as json_file:
  json.dump(turn_to_json, json_file)


data_payload = [
  {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
   'follow up': 'But enough talk!'}
]

with open('./output_files/data.json', 'w') as data_json:
  json.dump(data_payload, data_json)