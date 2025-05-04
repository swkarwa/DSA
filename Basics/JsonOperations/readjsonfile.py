import json
import os

jsonString = """
{"menu": {
  "id": "file",
  "value": "File",
  "popup": {
    "menuitem": [
      {"value": "New", "onclick": "CreateNewDoc()"},
      {"value": "Open", "onclick": "OpenDoc()"},
      {"value": "Close", "onclick": "CloseDoc()"}
    ]
  }
}}
"""


def readJsonFile():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_file = current_dir + "/sample.json"
    with open(json_file, "r") as file:
        data = json.load(file)  # read json file and convert to dict
        print(data)
        print(type(data))

def readJsonString():
    dict_data = json.loads(jsonString)
    print(dict_data)
    print(type(dict_data))


# readJsonFile()
readJsonString()