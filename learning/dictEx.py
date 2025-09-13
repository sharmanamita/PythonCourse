dictionary = {"name": "namita", "surname": "Sharma", "address": { "city": "Pune", "pin": "33338"}}

x = dictionary['name']
print(x)

y = dictionary.keys()
print(y)

z = dictionary.values()
print(z)

for key in dictionary:
    print(dictionary[key])
    if key == "address":
        print(dictionary[key]["pin"])

items = dictionary.items()

for tuple in items:
    print("key: ", tuple[0], "value: ", tuple[1])

del dictionary["address"]['pin']
print(dictionary)

dictionary.clear()
print(dictionary)

dictionary["product"] = "pencil"
dictionary["brand"] = "Natraj"

dictionary.update({"product": "pen"})
dictionary.update({"cost": 10})

# del dictionary
print(dictionary)