# Write a function to convert a number
# entered by the user into its corresponding
# number in words. For example, if the input
# is 876 then the output should be
# ‘Eight hundred Seventy Six’.
def three_num(num, ending):
    international = ["", "thousand", "million", "billion", "trillion", "quadrillion",
                     "quintillion", "sextillion", "Octillion", "nonillion", "decillion",
                     "undecillion", "tredecillion", ]
    numberNames = {"0": '', "1": 'One', "2": 'Two', "3": 'Three', "4": 'Four',
                   "5": 'Five', "6": 'Six', "7": 'Seven', "8": 'Eight', "9": 'Nine'}
    appendage = [" ", "ty ", " hundred", ]
    appendage1s = ["ten", "eleven", "twelve", "thirteen", "fourteen",
                   "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    appendage10s = ["twenty", "thirty", "forty", "fifty",
                    "sixty", "seventy", "eighty", "ninety"]
    num = list(num)
    iterlist = tuple(num)
    num.reverse()
    length = len(num)
    for a in range(length):
        if num[a] != "0":
            num[a] = numberNames[num[a]] + appendage[a]
    if len(iterlist) > 1 and '1' == iterlist[-2]:
        del num[-2]
        num[0] = appendage1s[int(iterlist[-1])]
    elif len(iterlist) > 2 and '1' == iterlist[-2]:
        num[-2] = "and " + appendage10s[int(iterlist[-2]) - 2]
    elif len(iterlist) == 2 and '1' == iterlist[-2]:
        num[-2]= appendage10s[int(iterlist[-2]) - 2]
    elif len(iterlist) == 2 and not '1' == iterlist[-2]:
        num[-1] = appendage10s[int(iterlist[-2]) - 2]
    elif len(iterlist) > 2 and not '1' == iterlist[-2] and not iterlist[-1] == "0" and not iterlist[-2] == "0":
        num[-2] = "and " + appendage10s[int(iterlist[-2]) - 2]
    num = [value for value in num if value != "0"]
    num.reverse()
    num = num + [international[ending], ]
    return num


print('''This program can print up to 42 digits worth of answers 
    
please use the input to give your number and Enter exit to stop
    
    ''')

s = True

while s:
    inp = input("Number or Enter exit: ")
    if inp == "exit":
        exit(0)
    if inp == "0" :
        print("Zero")
    inp = inp + '0'
    inplist = []
    result = []
    ending = 0
    for i in range(1, 1 * (len(list(inp))), 3):
        inplist.insert(0, inp[-(i + 3): -i])
    for i in range(1, len(inplist) + 1):

        if inplist[-i] == "000" or inplist[-i] == "0" or inplist[-1] == "00":
            ending +=1
        else:
            result = three_num(inplist[-i], ending) + result
            ending += 1
    string_result = ' '.join(result)

    print(string_result)
