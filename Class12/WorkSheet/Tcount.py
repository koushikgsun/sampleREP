def Tcount():
    count = 0
    for i in open("Rank.txt").read().split() :
        if i[0] in 'Tt' : count += 1
    print (count)