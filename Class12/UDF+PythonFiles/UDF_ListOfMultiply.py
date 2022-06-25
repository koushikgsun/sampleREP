def Listmul(lister):
    muk = 0
    for i in lister:
        muk += i
    return muk


y = []
while True:
    num = input("Enter number/ exit/ M : ")
    if num == "exit":
        exit(0)
    elif num == "M":
        print(Listmul(y))
    else:
        y.append(int(num))