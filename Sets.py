# A set is a collection which is unordered, unchangeable (can still add/remove) and unindexed and don't allow duplicates
# The values True and 1 are considered same in the set. Only one of them will be printed
# The values False and 0 are considered same in the set. Only one of them will be printed

# set1 = {"Item1", "Item2", 1, True, "Item3", "Item4"}
# print(set1)
# print(set1)
#
# print(len(set1))
#
#
#
# # Access set items - Can't access items in a set by index.
# for x in set1:
#     print(x)
# # Check if an item is present
# print("Item3" in set1)
# print("Sam" not in set1)
#



# Add Items
# set2 = {"India", "Pakistan", "Russia", "China", "UAE"}
# set2.add("England")     # Adds one item
# print(set2)
#
# sports = {"Hockey", "Cricket"}
# set2.update(sports)     # Add items from other iterables to the current set
# print(set2)




# Remove items - remove will raise an error if the item is not present in the set, but using discard method
# will not raise an error
# set4 = {"Virat", "Dhoni", "Rohit", "Bumrah"}
# set4.remove("Rohit")
# print(set4)
# The clear method empties the set
# set4.clear()
# print(set4)
# del will delete the set completely



# Loop sets
# for name in set4:
#     print(name)



# Join sets
# The union() and update() method joins all the items from both sets
# The intersection() method only keeps the duplicates
# The difference() method keeps the items from the first set that are not in the other set(s).
# The symmetric_difference() method keeps all items EXCEPT the duplicates.

odd_set = {1, 3, 5, 7}
even_set = {2, 4, 6, 8}
multiple_3 = {3, 6, 9}

# the union method allows you to join a set with other data types, like lists, tuples. The result will be a set
union_set = odd_set.union(even_set)
union_set1 = odd_set.union(multiple_3)
print(union_set)
print(union_set1)


# Intersection
intersection_set = odd_set.intersection(even_set)
print("Intersection:", intersection_set)


# Difference - returns a new set that contains only the items from the first set that are not present in the other
cities1 = {"Lahore", "Islamabad", "Karachi", "Multan"}
cities2 = {"Lahore", "Peshawar", "Gujarat", "Karachi"}
cities3 = cities1.difference(cities2)
print("Difference:", cities3)
