import os, time

#splits dictionary into separate lists
def dic_to_lists(Pdicto):
    list_title= []
    for i in Pdicto:
        list_title.append(i)   
    return list_title

#converts all lists back into dictionary
def lists_to_dic(Plist,PIlist,Pchoice):
    for x in range(len(Plist)):
        if int(Pchoice) == x:
            dicto[Plist[x]] = PIlist

#add item to a list
def add_to_list(Pchoice, Plist):    
    if Pchoice not in Plist:
        Plist.append(Pchoice)
    if "blank list" in Plist:
            Plist.pop(0)
            
#checks for keys in dictionaru, if none makes a blank one.
def blank_dic(Pdicto):
    if not Pdicto:
        Pdicto["blank"]=[]
        return Pdicto

#checks for a blank list, if it is adds blank to list
def blank_list(Plist):
    if not Plist:
        Plist=["blank list"]
    return Plist

#print out list with index
def print_num_list(Plist):
    #point used to increase list index
    point=0
    os.system("clear")
    for i in Plist:
        print(str(Plist.index(i)) +":"+i)
        point+= 1

#if the input is blank
def empty_choice(Pchoice):
    if not Pchoice:
        print("Not a valid choice.")
        time. sleep(.5)
        return True

#adds key to list for dictionary
def add_new_list(Pdicto,Pchoice):
    Pdicto[Pchoice]=[]
    print("Added!")
    time.sleep(.5)
    if "blank" in Pdicto:
        Pdicto.pop("blank")

#to select key from dictionary to display as list
def select_list(Pdicto, Pchoice, Plist):
    for x in range(len(Plist)):
        if int(Pchoice) == int(x):
            #stores list of choice as y
            return Pdicto[Plist[int(Pchoice)]]

#delete a key from dictionary
def delete_list(Pchoice, Plist):
    if "delete" in Pchoice:
        d = input("Delete mode\nEnter list to delete.\n")
        try:
            AYS = input(f"""Are you sure? 
delete {d}
'yes' or 'no'?""")
            #if user enters 'yes'
            if AYS in "yes":
                Plist.pop(d)
                return True
            #if user enters 'no'
            else:
                return True
        except:
            print("invalid")
            return True

#delete item from a list
def delete_item(Pchoice,Pindex,Plist):
    if int(Pchoice) == Pindex:
        Plist.pop(int(Pchoice))
    return Plist


#go back from selected list
def return_to_main(Pchoice):
    if Pchoice == "b":
        return True

#save dictionary to file
def save_list(Pdicto):
    print("saved")
    with open("todo.txt", "w") as f:
        f.write(str(Pdicto))
    return True

#input text 0
main_choice="""\nEnter a number to select list.
Enter a title for a new list.
Enter 'delete' to start delete mode.\n"""

#input text 1
list_choice="""\nEnter a task to add.
Enter task number to delete task.
Enter 'b' to go to main menu.\n"""

#checks for'todo.txt' and make one of doesn't exist.
def check_for_file():
        try:
            #checks for todo.txt
            dicto = eval(open("todo.txt",).read())
            return dicto
        except:
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
    pin1= True
    
    list_title = dic_to_lists(dicto)
        
    print_num_list(list_title)

#select or modify menu
    choice0 = input(main_choice).strip()

#start input checks    

#if nothing is entered 
    if empty_choice(choice0):
        continue

    if delete_list(choice0, dicto):
        continue
    
    
#start on inner list
    try:
#assign dictionary value to variable
        in_list = select_list(dicto, choice0, list_title)

#start of second loop
        while pin1:
            
#checks if list is empty
            in_list = blank_list(in_list)
            
            #print title of selected list
            
            
            print_num_list(in_list)
            
#choice for modifying list
            choice1 = input(list_choice).strip()
              
#start input checks   
            for list_index in range(len(in_list)):

                if return_to_main(choice1):
                    pin1= False
                    break
                                        
                try:
                    delete_item(choice1,list_index,in_list)
                
                except:
                    if empty_choice(choice1):
                        continue

                    add_to_list(choice1,in_list)
                    
                    lists_to_dic(list_title, in_list, choice0)
                   # continue
                                
    except:
        add_new_list(dicto,choice0)

      

if __name__ == "__main__":
    main()











