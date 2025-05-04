import json

# expected_json = """
# [
#   {
#     "Id": 125,
#     "Expected_first_name": "Shyam",
#     "Expected_middle_name": "C",
#     "Expected_last_name": "Basu",
#     "Expected_address": "Flat No. 1; Bengaluru",
#     "Expected_salary": 2500000,
#     "Expected_location": "Marathahalli"
#   },
#   {
#     "Id": 27,
#     "Expected_first_name": "Ram",
#     "Expected_middle_name": "A",
#     "Expected_last_name": "Kumar",
#     "Expected_address": "Flat No. 2; Bengaluru",
#     "Expected_salary": 3000000,
#     "Expected_location": "Indiranagar"
#   },
#   {
#     "Id": 31,
#     "Expected_first_name": "Hari",
#     "Expected_middle_name": "D",
#     "Expected_last_name": "Sharma",
#     "Expected_address": "Flat No. 3; Bengaluru",
#     "Expected_salary": 5000000,
#     "Expected_location": "Indiranagar"
#   },
#   {
#     "Id": 145,
#     "Expected_first_name": "Raj",
#     "Expected_middle_name": "S",
#     "Expected_last_name": "Mani",
#     "Expected_address": "Flat No. 41; Bengaluru",
#     "Expected_salary": 4000000,
#     "Expected_location": "Sarjapur"
#   },
#   {
#     "Id": 5,
#     "Expected_first_name": "Kumar",
#     "Expected_middle_name": "B",
#     "Expected_last_name": "Adarsh",
#     "Expected_address": "Flat No. 5; Bengaluru",
#     "Expected_salary": 4000000,
#     "Expected_location": "JP Nagar"
#   }
# ]
# """
#
# actual_json = """
# [
#   {
#     "Id": 27,
#     "Actual_first_name": "Ram",
#     "Actual_middle_name": "",
#     "Actual_last_name": "Kumar",
#     "Actual_address": "Flat No. 2; Bengaluru",
#     "Actual_salary": 3000000,
#     "Actual_location": "Indiranagar"
#   },
#   {
#     "Id": 31,
#     "Actual_first_name": "Hari",
#     "Actual_middle_name": "D",
#     "Actual_last_name": "Sharma",
#     "Actual_address": "Flat No. 3; Bengaluru",
#     "Actual_salary": 5000000,
#     "Actual_location": ""
#   },
#   {
#     "Id": 5,
#     "Actual_first_name": "Kumar",
#     "Actual_middle_name": "",
#     "Actual_last_name": "Adarsh",
#     "Actual_address": "Flat No. 5; Bengaluru",
#     "Actual_salary": "",
#     "Actual_location": "JP Nagar"
#   },
#   {
#     "Id": 125,
#     "Actual_first_name": "Shyam",
#     "Actual_middle_name": "",
#     "Actual_last_name": "Basu",
#     "Actual_address": "Flat No. 1; Bengaluru",
#     "Actual_salary": 2500000,
#     "Actual_location": "Marathahalli"
#   },
#   {
#     "Id": 145,
#     "Actual_first_name": "Raj",
#     "Actual_middle_name": "S",
#     "Actual_last_name": "Mani",
#     "Actual_address": "",
#     "Actual_salary": 4000000,
#     "Actual_location": "Sarjapur"
#   }
# ]
#
# """

expected_json = """
[
  {
    "Id": 125,
    "Expected_first_name": "Shyam",
    "Expected_middle_name": "C",
    "Expected_last_name": "Basu",
    "Expected_address": "Flat No. 1; Bengaluru",
    "Expected_salary": 2500000,
    "Expected_location": "Marathahalli",
    "Fields_to_be_verified": [
      "Expected_first_name",
      "Expected_middle_name",
      "Expected_last_name",
      "Expected_address",
      "Expected_salary",
      "Expected_location"
    ]
  },
  {
    "Id": 27,
    "Expected_first_name": "Ram",
    "Expected_middle_name": "A",
    "Expected_last_name": "Kumar",
    "Expected_address": "Flat No. 2; Bengaluru",
    "Expected_salary": 3000000,
    "Expected_location": "Indiranagar",
    "Fields_to_be_verified": [
      "Expected_first_name",
      "Expected_last_name",
      "Expected_address",
      "Expected_salary",
      "Expected_location"
    ]
  },
  {
    "Id": 31,
    "Expected_first_name": "Hari",
    "Expected_middle_name": "D",
    "Expected_last_name": "Sharma",
    "Expected_address": "Flat No. 3; Bengaluru",
    "Expected_salary": 5000000,
    "Expected_location": "Indiranagar",
    "Fields_to_be_verified": [
      "Expected_first_name",
      "Expected middle name",
      "Expected_last_name",
      "Expected_address",
      "Expected_salary"
    ]
  },
  {
    "Id": 145,
    "Expected_first_name": "Raj",
    "Expected_middle_name": "S",
    "Expected_last_name": "Mani",
    "Expected_address": "Flat No. 41; Bengaluru",
    "Expected_salary": 4000000,
    "Expected_location": "Sarjapur",
    "Fields_to_be_verified": [
      "Expected_first_name",
      "Expected middle name",
      "Expected_last_name",
      "Expected_salary"
    ]
  },
  {
    "Id": 5,
    "Expected_first_name": "Kumar",
    "Expected_middle_name": "B",
    "Expected_last_name": "Adarsh",
    "Expected_address": "Flat No. 5; Bengaluru",
    "Expected_salary": 4000000,
    "Expected_location": "JP Nagar",
    "Fields_to_be_verified": [
      "Expected_first_name",
      "Expected_last_name",
      "Expected_address",
      "Expected_location"
    ]
  }
]
"""

actual_json = """
[
  {
    "Id": 27,
    "Actual_first_name": "Ram",
    "Actual_middle_name": "",
    "Actual_last_name": "Kumar",
    "Actual_address": "Flat No. 2; Bengaluru",
    "Actual_salary": 3000000,
    "Actual_location": "Indiranagar"
  },
  {
    "Id": 31,
    "Actual_first_name": "Hari",
    "Actual_middle_name": "D",
    "Actual_last_name": "Sharma",
    "Actual_address": "Flat No. 3; Bengaluru",
    "Actual_salary": 5000000,
    "Actual_location": ""
  },
  {
    "Id": 5,
    "Actual_first_name": "Kumar",
    "Actual_middle_name": "",
    "Actual_last_name": "Adarsh",
    "Actual_address": "Flat No. 5; Bengaluru",
    "Actual_salary": "",
    "Actual_location": "JP Nagar"
  },
  {
    "Id": 125,
    "Actual_first_name": "Shyam",
    "Actual_middle_name": "",
    "Actual_last_name": "Basu",
    "Actual_address": "Flat No. 1; Bengaluru",
    "Actual_salary": 2500000,
    "Actual_location": "Marathahalli"
  },
  {
    "Id": 145,
    "Actual_first_name": "Raj",
    "Actual_middle_name": "S",
    "Actual_last_name": "Mani",
    "Actual_address": "",
    "Actual_salary": 4000000,
    "Actual_location": "Sarjapur"
  }
]

"""

expected_data = json.loads(expected_json)
actual_data = json.loads(actual_json)

expected_ids = []
for item in expected_data:
    expected_ids.append(item.get("Id"))

for expected_item in expected_data:
    for actul_item in actual_data:
        if (expected_item.get("Id") == actul_item.get("Id")):
            # perform comparison
            for key in expected_item.get("Fields_to_be_verified"):
                if( not actul_item.get("Actual_"+key[9:]) == expected_item.get(key)):
                    print( key + " mismatched for id "+ str(actul_item.get("Id")))
