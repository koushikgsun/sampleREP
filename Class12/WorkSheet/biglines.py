def BIGLINES():
    count = 0
    for i in open("CONTENT.txt").readlines():
        if len(i) >20 : count+= 1
    print("Count of BIGLINES is : ", count)