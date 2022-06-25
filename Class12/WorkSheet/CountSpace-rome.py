def countSpace():
    count = 0
    for i in open("ROME.txt", "r").read() :
        if i == " ":
            count +=1
    return count
