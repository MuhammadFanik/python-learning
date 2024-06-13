msg1 = "Sam is a student"
# access elements in a string
# print(msg1[2])
# # to get the length of the string, use len() function
# print(len(msg1))
# # To check if a certain phrase or character is present in a string
# print("Sam" in msg1)
# print("Smith" in msg1)
# # To check if a certain phrase or character is not present in a string
# print("Warner" not in msg1)
#
#
# #Slicing strings
# print(msg1[1:11])  # Starts slicing the string from index 1(included) till index 11(excluded)
# print(msg1[-7:-1])
#
#
# # Modify Strings
# print(msg1.upper()) # converts it into upper case
# print(msg1.lower()) # converts it into lower case
# print(msg1.strip()) # removes any whitespaces in the start and end
# print(msg1.replace("student", "teacher"))   # replace method replaces a string with another string
# print(msg1.split(" ")) # returns a list where the text between the specified character (space) in this case
#
#
# # Concatenate strings
# msg2 = "This is message 2"
# print(msg1+ " " + msg2)
#
#
# # Playing with strings
# myString1 = "Fanik"
# myString2 = myString1
# upperString = myString2.upper()
#
# print(myString1)
# print(upperString)
# print(myString1)    # Fanik
# print(myString2)    # Fanik
#
#
name = "tariq"
print(name.capitalize())    # converts the first character to uppercase character
print(name.casefold())  # Converts a string into lowercase

