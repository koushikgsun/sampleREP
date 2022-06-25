print("Try block initiating..... ")
try:
    numerator = 50
    denominator = int(input("Enter the denominator : "))
    quotient = numerator/denominator
    print("Division performed successfully")
except ZeroDivisionError:
    print ("Denominator as ZERO.... not allowed")
print("terminated")
