import json

myDict = {"boolean value": True}
myDictJsonVal = json.dumps(myDict)
print(myDictJsonVal)
myDictNormalVal = json.loads(myDictJsonVal)
print(myDictNormalVal)