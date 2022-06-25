def countSpace():
    count = 0
    for i in open("CONTENT.txt", "r").read() :
        if i == " ":
            count +=1
    return count