print("Try block with multiple handling initiating..... ")
try:
    numerator = 50
    denominator = int(input("Enter the denominator : "))
    print(numerator/denominator)
    print("Division performed successfully")
except ZeroDivisionError:
    print("Denominator as ZERO.... not allowed")
except :
    print("some Error or the Other Error Occurred lmao")