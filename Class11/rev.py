def Listmul(lister):
    muk = ''
    for i in range(1, len(lister) + 1):
        muk = muk + lister[-i]
    return muk


y = ""
while True:
    num = input("Enter number/ exit/ M : ")
    if num == "exit":
        exit(0)
    else:
        print(Listmul(num))