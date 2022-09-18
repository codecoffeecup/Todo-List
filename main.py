import Task

#input text 0
main_choice = """\nEnter list name to select
Enter a title for a new list.
Enter 'delete' to start delete mode.\n"""

#input text 1
list_choice = """\nEnter a task to add.
Enter task number to delete task.
Enter 'b' to go to main menu.\n"""

dd=Task.lists()

#main loop
def main():

  while True:

    dd.blank_dict()
    #dd.get_dict()

    #reset key to run second loop
    pin1 = True
    dd.print_lists()
    choice0 = input(main_choice).strip()
    #start input checks
    if dd.empty_choice(choice0):
        continue

    if choice0.lower() == "delete": 
        dd.delete_list(choice0)
        continue
        
    #start on inner list
    try:
        #start of second loop
        while pin1:
            dd.blank_list(choice0)
            dd.print_tasks(choice0)
            choice1 = input(list_choice).strip()              
            #start input checks
            if dd.main_menu(choice1):
                pin1 = False
                continue
            try:
                dd.delete_item(choice0,choice1)            
            except ValueError:
                if dd.empty_choice(choice1):
                    continue
                dd.add_to_list(choice1,choice0)
                dd.save_dict()
    except KeyError:
        dd.add_new_list(choice0)
        dd.save_dict()

if __name__ == "__main__":
    main()

