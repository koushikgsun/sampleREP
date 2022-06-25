# Write a function to convert a number
# entered by the user into its corresponding
# number in words. For example, if the input
# is 876 then the output should be
# ‘Eight Seven Six’.
result = ""
numberNames = {"0": 'Zero', "1": 'One', "2": 'Two', "3": 'Three', "4": 'Four',
               "5": 'Five', "6": 'Six', "7": 'Seven', "8": 'Eight', "9": 'Nine'}
x = input("Number : ")
for i in x:
    result = result + numberNames[i] + " "
print(result)
