import json

with open('data.json') as json_file:
    data = json.load(json_file)
    data_max = max(data['Subscriptions'], key=lambda i: i['price'])
    # parsed = json.dumps(data_max)
    Name = data_max.get('name', "")
    Price = data_max.get('price', "")
    print("Name:", Name)
    print("Price:", Price)

for i in data['Subscriptions']:
    print("Name:", (i['name']))
    print("Price:", (i['price']))


# your_json = '["foo", {"bar":["baz", null, 1.0, 2]}]'
# parsed = json.loads(your_json)
# print(json.dumps(parsed, indent=4, sort_keys=True))
