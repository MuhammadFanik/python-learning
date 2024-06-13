# Lists are used to store multiple items in a single variable
# List items are ordered, changeable(change, add, or remove items) and allow duplicates
# indiaList = ["Rohit", "Virat", "Bumrah", "Hardik", "Babar", "Rohit"]
#
# print(indiaList)
# print(len(indiaList))   # How many items present in the list, use len function
# print(type(indiaList))
#
#
# # Access list items
# # This returns a new list with the specified items
# print(indiaList[2])     # Bumrah
# print(indiaList[1:4])   # Virat Bumrah Hardik
#
#
# # Check if item exists
# if "Virat" in indiaList:
#     print("Virat is present in the team")
#
#
# # Change List items
# indiaList[1] = "Siraj"      # This will change the value at index 1 to Siraj
# print(indiaList)
# indiaList[3:5] = ["Rinku", "Kuldeep"]   # Change a range of item values
# print(indiaList)
#
#
# # Insert Items
# indiaList.insert(5, "Dhoni")    # Inserts a new list item, without replacing any of the existing values
# print(indiaList)
#
#
# # Add list items
# fruitsList = ["Apple", "Banana", "Cherry", "Falsa", "Mango"]
# numbers = [2, 4, 7, 9, 1, 2]
#
# fruitsList.append("Lemon")      # Adds an item to the end of the list
# print(fruitsList)
# fruitsList.extend(numbers)      # Append elements from other list to the current list
# print(fruitsList)
#
#
#
# # Remove List Items
# numbers.remove(2)   # Removes the specified item (only the first instance)
# print(numbers)
# numbers.pop(2)      # Removes the element present at index 2. If index is not specified, it removes the last element
# print(numbers)
#
# # del keyword can delete the list completely
# # clear() method empties the list content, but the list still remains
# numbers.clear()
# print(numbers)
#
#
#
#
# # Loop lists
# names = ["Hassan", "Ahmad", "Umar", "Usman", "Taha"]
# for x in names:
#     print(x)
#
#
#
# # Sort lists
# names1 = ["India", "Pakistan", "australia", "Canada"]
# numbers1 = [5, 4, 7, 9, 3, 15, 12]
# numbers2 = [9, 7, 8, 4, 1, 2]
# names1.sort()   # It is case-sensitive, sorts capital letters before small letters.
# numbers1.sort()
# numbers2.sort(reverse=True)
# names1.sort(key=str.lower)      # Case Insensitive sort
#
# print(names1)
# print(numbers1)
# print(numbers2)
# print(names1)



# # Copy lists:  Use .copy() or list method
# subjects = ["Maths", "Physics", "Chemistry", "English"]
# copyList = subjects.copy()
# print(copyList)
#
# subjects[0] = "DSA"
# print(subjects)
#
# members = [2, 5, 7, 9, 13]
# newCopyList = list(members)
#
# members[1] = 88
# print(newCopyList)
# print(members)
#


# Join Lists
list1 = [2, 4, 6]
list2 = [1, 3, 5]
list3 = list1 + list2
print(list3)
print(type(list1))
