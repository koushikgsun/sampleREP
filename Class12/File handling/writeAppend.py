FH = open("Sample.txt", "w+")
while True :
    FH.write(input("enter data you want to save : "))
    ans = input("Do you wish to continue (Y/N) : ").lower()
    if ans == "n":
        break
FH.close()