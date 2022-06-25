def append(argument):
    mylist = mylist + [argument,]
def delete(argument):
    inDex = mylist.index(argument)
    newlist = mylist[0:inDex] + mylist[inDex+1:-1]
    return newlist

mylist = [1,2,3,4,5,6]
print(delete(3))
