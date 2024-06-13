# IT is ordered, changeable, and does not allow duplicates

# thisDict = {
#     "brand": "Toyota",
#     "name": "Corolla",
#     "year": 2020
# }
# print(thisDict)
# print(thisDict["name"])
# print(len(thisDict))
#
# # Access Items
# # Keys method - returns a list of all the keys in the dictionary, and it is live
# keys = thisDict.keys()
# print(keys)
# # Values method returns a list of all the values in the dictionary, and it is live
# values = thisDict.values()
# print(values)
# # items method - returns each item in the dictionary as tuples in a list, and it is live
# items = thisDict.items()
# print(items)
# # check if key exists
# if "make" in thisDict:
#     print("make exists in the dictionary")
# else:
#     print("Make does not exist")
#
#
#
# # Change Items
# dict1 = {"name": "Sam", "age": 30, "color": "white"}
# print(dict1)
#
# # Add items
# dict1["birth"] = "USA"
# print(dict1)
#
# # Remove Items
# # pop method, popitem method removes the last inserted item
# # clear method empties the dictionary
# dict1.pop("age")    # removes age
# print(dict1)
#
#
#
# # Looping in dictionaries
# dict2 = {
#     "name": "Umar",
#     "age": 18,
#     "student": True
# }
# # this will print all the keys in the dictionary
# print("Keys in the dict2")
# for keys in dict2:
#     print(keys)
# # this will print all the keys in the dictionary
# print("Values in the dict2")
# for values in dict2:
#     print(dict2[values])




# Copy dictionary - use the copy method or the dict() method
dict3 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
copy_dict = dict3.copy()
print(dict3)
print(copy_dict)
