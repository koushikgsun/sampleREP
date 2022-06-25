top = int(input("the ceiling : "))
low = int(input("the lowing : "))

while True:
    test = int(input("Enter Test : "))
    if test in range(low, top + 1) :
        print("positive")
    else:
        print( "negative")