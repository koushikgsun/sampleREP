# Create a dictionary ‘ODD’ of odd numbers between 1 and 10, where the
# key is the decimal number and the value is the corresponding number
# in words. Perform the following operations on this dictionary:
# (a) Display the keys
# (b) Display the values
# (c) Display the items
# (d) Find the length of the dictionary
# (e) Check if 7 is present or not
# (f) Check if 2 is present or not
# (g) Retrieve the value corresponding to the key 9
# (h) Delete the item from the dictionary corresponding to the key 9
ODD = {1: "one", 3: "three", 5: "five", 7: "seven", 9: "nine"}
print("(a) ", ODD.keys())
print("(b) ", ODD.values())
print("(c) ", ODD)
print("(d) ", len(ODD))
if 7 in ODD.keys():
    print("(e)  YES")
else:
    print("(e)  NO")
if 2 not in ODD.keys():
    print("(f)  NO")
else:
    print("(f)  YES")
print("(g) ", ODD[9])