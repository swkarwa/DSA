dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

## access values
print(dict["name"])

# inserting and updating values
dict["email"] = "skarwa4491@gmail.com"
dict["city"] = "updated city"
print(dict)

# removing item
dict.pop("email")
# dict.popitem() # removes lst KV pair from dict
print(dict)

print(dict.keys()) # get all keys
print(dict.values()) # get all values

# dict comprehension
c_dict = {x : x**2 for x in range(5)}
print(c_dict)

# nested dict
nested_dict = {
    "person": {
        "name": "Alice",
        "age": 30
    },
    "address": {
        "city": "New York",
        "zip": "10001"
    }
}

# get default value
print(nested_dict.get("email" , "not provided"))
