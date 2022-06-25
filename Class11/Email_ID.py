# 1.Write a program to read email IDs of n number of students and store them in a tuple. Create two
# new tuples, one to store only the usernames from the email IDs and second to store domain names
# from the email IDs. Print all three tuples at the end of the program. [Hint: You may use the function split()]
x = True
tuple1 = tuple()
tuple2 = tuple()
tuple3 = tuple()
while x:
    Input = input("Please enter email id : ")
    tuple1 = tuple1 + (Input, )
    for i in Input:
        if i == "@":
            atindex = Input.index('@')
            tuple2 = tuple2 + (Input[0: atindex], )
            tuple3 = tuple3 + (Input[atindex:], )
    if Input == "end" :
        break

print("Email ID__|__Username_|_Domain")
for i in range(0,len(tuple1)-1):

    print (tuple1[i],"__|__", tuple2[i],"_|_", tuple3[i])
