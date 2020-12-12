import json

myJSONstring = '{"Hello":"There"}'
print(type(myJSONstring))
myDictionary = json.loads(myJSONstring)
print(type(myDictionary))
print(myDictionary.Hello)