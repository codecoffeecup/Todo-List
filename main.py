import os, time

class lists():
    def __init__(self):
        try:
            self.dict = eval(open("todo.txt",).read())
        except FileNotFoundError:
            with open("todo.txt","w") as f:
                f.write(str({"todo":[]}))
                dict = eval(open("todo.txt").read())



    def get_dict(self):
        #with "todo.txt" as f:
        self.dict = eval(open("todo.txt").read())
        return dict

    def print_lists(self):
        point=0
        os.system("clear")
        for k in self.dict.keys():
            print(str(point)+":"+k)
            point+=1


    def delete_list(self, choice):
         d = input(delete_choice)
         for k in list(self.dict):
              if d.lower() == k.lower():
                  self.dict.pop(d)
                  break 
         dd.save_dict()


    def print_tasks(self, choice):
        point = 0
        os.system("clear")
        for v in self.dict[choice]:
            print(str(point) + ":" + str(v))
            point += 1

    def add_new_list(self, choice):
        self.dict[choice]=[]
        print("List added")
        time.sleep(2)
        if "blank" in self.dict:
            dicto.pop("blank")
        dd.save_dict()

    def add_to_list(self, task, choice0):
        self.task = task
        if self.task not in self.dict[choice0]:
            self.dict[choice0].append(self.task)
        if "blank" in self.dict[choice0]:
            self.dict[choice0].pop(0)
        dd.save_dict()

    def save_dict(self):
        with open("todo.txt", "w") as f:
            f.write(str(self.dict))

    def blank_dict(self):
        if not self.dict:
            self.dict["Blank"]=[]
            return dict

    def empty_choice(self, choice):
        if not choice:                 
            print("Not a valid choice.")
            time. sleep(.5)
            return True

    def blank_list(self, choice):
        if not self.dict[choice]:
            self.dict[choice]= ["blank"]

    def main_menu(self, choice):
        if choice == "b":
            return True

    def delete_item(self, choice0, choice1):
        point = 0
        for v in self.dict[choice0]:
            if int(choice1) == point:
                self.dict[choice0].pop(point)
                point+=1
            else:
                point+=1
        dd.save_dict()


#input text 0
main_choice = """\nEnter list name to select
Enter a title for a new list.
Enter 'delete' to start delete mode.\n"""

#input text 1
list_choice = """\nEnter a task to add.
Enter task number to delete task.
Enter 'b' to go to main menu.\n"""

#input text 2
delete_choice = """Delete mode\nEnter list to delete.\n"""


dd=lists()

#main loop
def main():

  while True:

    dd.blank_dict()
    dd.get_dict()

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











