# Tuple is ordered and unchangeable(cant change, add or remove items) and allow duplicate values
# Tuple items can be of any data type and a tuple can contain different data types
tuple1 = (2, 4, 6, 8, 4)
print(tuple1)

tuple1_length = len(tuple1)
print(tuple1_length)    # Gives the length of the tuple
print(type(tuple1))     # Returns the type of the tuple


# Access tuple items
print(tuple1[2])
# Check if item exists
if 4 in tuple1:
    print("4 exists in this tuple")



# Update tuples - Tuples cannot be directly updated, convert it into a list, change it and then convert it back to a tuple
# Change tuple values
tuple2 = ("India", "Pakistan", "Srilanka", "Germany", "Spain")
# tuple2_list = list(tuple2)      # Converts it into a list
# tuple2_list[2] = "Russia"
# tuple2 = tuple(tuple2_list)
# print(tuple2)
# print(type(tuple2))

# Add items - 1: Convert it into a list, 2 Add tuple to a tuple
new_Tuple = ("China",)
tuple2 += new_Tuple
print(tuple2)

# Remove items: convert it into a list and then convert it back




# Unpack a tuple
# The * assigns the rest of the values to sports and returns it as a list
tuple3 = ("Apple", "Mango", "Falsa", "Cricket", "Football", "Hockey", "Swimming")
(red, yellow, purple, *sports) = tuple3
print(red)
print(yellow)
print(purple)
print(sports)



# Loop tuples
for x in tuple3:
    print(x)



# Join tuples
fruit_tuple = ("f1", "f2", "f3")
numbers_tuple = (2, 4, 6)
join_tuple = fruit_tuple + numbers_tuple
print(join_tuple)
multiple_tuple = numbers_tuple * 3
print(multiple_tuple)
