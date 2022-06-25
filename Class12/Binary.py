import pickle
def CREATE_REC():
    try:
        file = open("TEACHER.DAT", "ab+")
        while True:
            teacher = [input("Enter No. : "), input("Enter Name : "), input("Enter Salary : "),
                       input("Enter Department : "), input("Enter Gender : ")]
            pickle.dump(teacher, file)
            if input("Continue ? (y/n) : ") in "nN": break
    except EOFError:
        file.close()


def SEARCH_REC():
    while True:
        try:
            file = open("TEACHER.DAT", "rb+")
            while True:
                name = input("Enter Name : ")
                while True :
                    selection = pickle.load(file)[1]
                    if name == selection:
                        print("Found")
                        break
        except :
            print("No Such Teacher")
            file.close()
        if input("continue (y/n) : ") in "nN" : break

SEARCH_REC()
