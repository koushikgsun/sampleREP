# Write a program to input names of n students and store them in a
# tuple. Also, input a name from the user and find if this student
# is present in the tuple or not.
# We can accomplish these by:
# (a) writing a user defined function
# (b) using the built-in function
x = True
print("Menu: \n 1. Enter student name to add \n 2. Find \n 3. End")
tuple1 = tuple()
while x:
    Input = input("Enter command : ")
    tuple1 = tuple1 + (Input, )
    if Input == "end":
        exit()
    elif Input == "find":
        print("Menu \n 1. Input the student name to find \n 2. stop find")
        while x:
            command = input("Please enter student name to find : ")
            if command in tuple1:
                print("Yes")
            else:
                if command == "stop find":
                    break
                print("No")


