def function(Command_Given, Argument, Main_list):
    if Command_Given == "add" :
        Main_list.append(Argument)
    elif Command_Given == "append" :
        Main_list.append(Argument)
    elif Command_Given == "insert" :
        argum2 = int(input("insert index : "))
        Main_list.insert(argum2, Argument)
    elif Command_Given == "delete" :
        Main_list.remove(Argument)
    elif Command_Given == "max" :
        List_Modifier_variable = Main_list[0]
        for i in range(0, len(Main_list)):
            if Main_list[i] > List_Modifier_variable:
                List_Modifier_variable = Main_list[i]
            print (List_Modifier_variable)
    elif Command_Given == "min" :
        List_Modifier_variable = Main_list[0]
        for i in range(0, len(Main_list)):
            if Main_list[i] < List_Modifier_variable:
                List_Modifier_variable = Main_list[i]
            print (List_Modifier_variable)
    elif Command_Given == "reverse" :
        Main_list.reverse()
    elif Command_Given == "print":
        print(Main_list)
    elif Command_Given == "exit":
        exit()
    elif Command_Given == "sort":
        print(Main_list.sorted())
    elif Command_Given == "slice":
        x = int(input("Start"))
        y = int(input("End"))
        Z = int(input("Step"))
        Sliced_list = Main_list[x:y:z]
        print(Sliced_list)
        return Sliced_list