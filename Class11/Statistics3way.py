import statistics


def mean(s):
    m = (statistics.mean(s))
    return m
def mode(s):
    m = (statistics.mode(s))
    return m
def median(s):
    m = (statistics.median(s))
    return m


main_list = []
# main:
print ("Menu :\n 1. Median \n 2. Mode \n 3. Mean \n 4. end")
control = True
while control:
    inp = input("add an integer : ")
    if inp == "end":
        control = False
    elif inp.lower() == "mode":
        print(mode(main_list))
    elif inp.lower() == "median":
        print(median(main_list))
    elif inp.lower() == "mean":
        print(mean(main_list))
    else:
        new_int = [int(inp)]
        main_list = main_list + new_int
