import os, time

#add item to a list
def add_to_list(choice0, choice1, dic):
    if choice1 not in dic[choice0]:
        dic[choice0].append(choice1)
    if "blank" in dic[choice0]:
        dic[choice0].pop(0)
            
#checks for keys in dictionaru, if none makes a blank one.
def blank_dic(dic):
    if not dic:
        dic["blank"]=[]
        return dic

#checks for a blank list, if it is adds blank to list
def blank_list(dic, choice):
    if not dic[choice]:
        dic[choice]= ["blank"]
    return True

#print out list with index
def print_num_list1(dicto):
    point= 0
    os.system("clear")
    for k in dicto:
        print(str(point)+":"+k)
        point+=1

def print_num_list2(dic, choice):
    point = 0
    os.system ("clear")
    print(choice)
    for v in dic[choice]:
        print (str(point)+":"+str(v))
        point+=1

#if the input is blank
def empty_choice(choice):
    if not choice:
        print("Not a valid choice.")
        time. sleep(.5)
        return True

#adds key to list for dictionary
def add_new_list(dic,choice):
    dic[choice]=[]
    print("Added!")
    time.sleep(.5)
    if "blank" in dic:
        dicto.pop("blank")

#delete a key from dictionary
def delete_list(choice, dic):
    if "delete" in choice:
        d = input("Delete mode\nEnter list to delete.\n")
        try:
            ya_sure = input(f"""Are you sure? 
delete {d}
'yes' or 'no'?""")
            #if user enters 'yes'
            if ya_sure.lower() in ("yes","y"):
                dic.pop(d)
                return True
            #if user enters 'no'
            else:
                return True
        #if choice isn't in list
        except KeyError:
            print("invalid")
            return True

#delete a task from a list in dictionary
def delete_task(choice0, choice1, dic):
    point = 0
    for v in dic[choice0]:
        if int(choice1) == point:
            dic[choice0].pop(point)
            point+=1
        else:
            point+=1

#go back from selected list
def return_to_main(choice):
    if choice == "b":
        return True

#save dictionary to file
def save_list(dic):
    print("saved")
    with open("todo.txt", "w") as f:
        f.write(str(dic))
    return True

#input text 0
main_choice = """\nEnter list name to select
Enter a title for a new list.
Enter 'delete' to start delete mode.\n"""

#input text 1
list_choice = """\nEnter a task to add.
Enter task number to delete task.
Enter 'b' to go to main menu.\n"""


#checks for'todo.txt' and make one of doesn't exist.
def check_for_file():
        try:
            #checks for todo.txt
            dicto = eval(open("todo.txt",).read())
            return dicto
        except FileNotFoundError:
            #if file doesn't exist, makes todo.txt in same directory as program.
            with open("todo.txt","w") as f:
                f.write(str({"todo":[]}))
            dicto = eval(open("todo.txt",).read())
            return dicto


#stores file as variable.   
dicto = check_for_file() 
    
#main loop
def main():
  while True:
    blank_dic(dicto)
    save_list(dicto)    
    #reset key to run second loop
    pin1 = True    
    print_num_list1(dicto)
    choice0 = input(main_choice).strip()
    #start input checks    
    if empty_choice(choice0):
        continue
    if delete_list(choice0, dicto):
        continue   
    #start on inner list
    try:
        #start of second loop
        while pin1:   
            blank_list(dicto, choice0)
            print_num_list2(dicto, choice0)        
            choice1 = input(list_choice).strip()              
            #start input checks  
            if return_to_main(choice1):
                pin1 = False
                continue                       
            try:
                delete_task(choice0,choice1,dicto)            
            except ValueError:
                if empty_choice(choice1):
                    continue 
                add_to_list(choice0, choice1, dicto)                             
    
    except KeyError:
        add_new_list(dicto,choice0)


if __name__ == "__main__":
    main()











