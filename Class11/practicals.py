class list_func:
    def __init__(self,arg):
        list_func.arg = arg
    def add(arg):
        list_main.append(arg)
    def delete(arg):
        if arg in list_main:
            list_main.remove(arg)
        else :
            print("no such value")
    def print():
        print(list_main)
list_main = []
print('''
List of commands :
Add
Delete
Print 
''')
while True :
    command = input("enter command or Exit : ")
    if command.lower() == "add":
        Item = input("Enter a item : ")
        list_func.add(Item)
    elif command.lower() == "delete" :
        Item = input("Enter an item : ")
        list_func.delete(Item)
    elif command.lower() == "print" :
        list_func.print()
    elif command.lower() == "exit" :
        exit(0)
    else:
        print("Wrong Command")