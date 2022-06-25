def ISTOUPcount():
    count = 0
    for i in open("WRITER.txt").read().split():
        if i in ['IS','UP','TO']: count+= 1
    print("Count of IS, UP and TO is: ", count)
