def pCOUNT():
    count = 0
    for i in open("BOOK.txt").readlines():
        if i[0] in "pP" : count+= 1
    print("Count of P/p is : ", count)