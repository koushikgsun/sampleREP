def AMCount():
    counta = 0
    countm = 0
    file = open("STORY.txt", "r").read()
    for i in file:
        if count in "aA": counta +=1
        if count in "mM": counta +=1
    print ("A or a : ", counta, "\n M or m : ", countm)