def ListSum(lister):
    sum = 0
    for i in lister:
        sum += i
    return sum


y = []
while True:
    num = input("Enter number/ exit/ Sum : ")
    if num == "exit":
        exit(0)
    elif num == "Sum":
        print(ListSum(y))
    else:
        y.append(int(num))