# This while loop starts from 1. On each iteration it checks if the value is equal to 6, if the value is not equal, it prints
# the value and then increments. If equal to 6, it will exit from the loop
iteration = 1
while (iteration < 5):
    print(iteration)
    iteration = iteration + 1
else:
    print("The value of iteration is not 4 anymore but its", iteration)




# For loop is used for iterating over a sequence(list, tuple, dict, string, set)
india = ["Virat", "Rohit", "Bumrah", "Hardik", "Arshdeep"]
for x in india:
    print(x)
else:
    print("Finished")   # Not executed if stopped by a break statement

for x in "Apple":
    print(x)

for x in range(2, 8, 3):   # Start the loop from 2 and finish at 7 with a step of 3
    print(x)

# For loops cannot be empty, but if you dont have any content, use the pass statement
