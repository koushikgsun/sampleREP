def acount():
    count = 0
    for i in open("A.txt").read().split() :
        if i[0] in 'aA' : count += 1
    print("Number of words starting with letter ‘a’ : ", count)