def CountConsonants():
    count = 0
    for i in open("AIM.txt", 'r').read():
        if i not in "AaEeIiOoUu":
            count += 1
    return count