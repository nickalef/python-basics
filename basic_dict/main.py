capitals = {"USA": "Washington D.C.", 
            "India": "New Delhi", 
            "China": "Beijing", 
            "Russia": "Moscow"}


print(capitals.get("USA"))

if capitals.get("Japan"):
    print("That capital exists")
else:
    print("That capital does not exist")

capitals.update({"Germany": "Berlin"})
capitals.update({"Russia": "Tokyo"})
print(capitals)
print("--------------------------")

capitals.pop("China")
capitals.popitem()
print(capitals)
print("--------------------------")

capital_keys = capitals.keys()
print(capital_keys)
print("--------------------------")

for key in capitals.keys():
    print(key)
print("--------------------------")

capital_values = capitals.values()
print(capital_values)
print("--------------------------")

for value in capitals.values():
    print(value)
print("--------------------------")

capital_items = capitals.items() # This returns a 2D list containing tuples
print(capital_items) 
print("--------------------------")
 
for key, value in capitals.items():
   print(f"{key} : {value}")