import os, time

#input text
delete_choice = """Delete mode\nEnter list to delete.\n"""

class lists():
    def __init__(self):
        try:
            self.dict = eval(open("todo.txt",).read())
        except:
            with open("todo.txt","w") as f:
                f.write(str({"todo":[]}))
            self.dict = eval(open("todo.txt").read())



    def get_dict(self):
        try:
            self.dict = eval(open("todo.txt").read())
        except FileNotFoundError:
            with open("todo.txt","w") as f:
                f.write(str({"todo":[]}))
                self.dict = eval(f).read()
       # return dict

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
         self.save_dict()


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
        self.save_dict()

    def add_to_list(self, task, choice0):
        self.task = task
        if self.task not in self.dict[choice0]:
            self.dict[choice0].append(self.task)
        if "blank" in self.dict[choice0]:
            self.dict[choice0].pop(0)
        self.save_dict()

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
        self.save_dict()
