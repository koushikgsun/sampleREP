print("Try block with multiple handling initiating..... ")
try:
    numerator = 50
    denominator = int(input("Enter the denominator : "))
    Damn = (numerator/denominator)
    print("Division performed successfully")
except ZeroDivisionError:
    print("Denominator as ZERO.... not allowed")
except ValueError:
    print("only Integers should be entered ")
else:
    print ("the result of division operation is ", Damn)