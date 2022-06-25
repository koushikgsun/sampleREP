# Write a program to enter names of
# employees and their salaries as input
# and store them in a dictionary.
import tabulate
dictionary = {}
print('''
Menu :
Enter name to add Employee
Enter name to add Salary
Enter exit in the Employee field to stop and print
     ''')
while True:
    x = input("Enter employee Name : ")
    if x.lower() == "exit":
        lists = list(dictionary.items())
        print(dictionary)
        exit(0)
    y = input("Enter employee Salary : ")
    dictionary[x] = y
