import json

json_string = """
{
  "books": [
    {
      "title": "The Great Gatsby",
      "author": "F. Scott Fitzgerald",
      "yearPublished": 1925,
      "genres": ["Fiction", "Classic"],
      "available": true
    },
    {
      "title": "1984",
      "author": "George Orwell",
      "yearPublished": 1949,
      "genres": ["Dystopian", "Science Fiction"],
      "available": false
    },
    {
      "title": "To Kill a Mockingbird",
      "author": "Harper Lee",
      "yearPublished": 1960,
      "genres": ["Fiction", "Drama"],
      "available": null
    }
  ]
}

"""

with open("sample.json" , 'r') as file:
    data = json.load(file)

print(type(data)) # dict

from_json_string = json.loads(json_string)
print(from_json_string) # dict

# convert to json string

s = json.dumps(from_json_string , indent=4)
print(s)