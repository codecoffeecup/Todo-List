#-*-coding:utf8;-*-
#qpy:console

#import modules
import os

#prints a numbered list
def pl (todo):
    for i in todo:
        print(str(todo.index(i)) + ": " + todo[todo.index(i)])
    with open("todo.txt","w") as f:
        f.write("\n".join(todo))

#delete item from list
def del_it(todo):
    todo.pop(int(choice))

#adds item to list, if blank fills in blank
def add_it(todo):
    todo.append(choice)
    if "blank" in todo:
        todo.pop(0)

#checks for text file, and create it off not found.
def check_file(list):
    try:
        open(list, "r")
    except:
        open(list, "w+")

check_file("todo.txt")

#stores text file as list
with open("todo.txt") as f:
    todo = f.read().splitlines()

#flow
while True:
    #clears screen
    os.system("clear")
    #fills in blank list
    if len(todo) == 0:
        todo.append("blank")
        continue  
    #prints list
    pl(todo)
    
    #variable used to add or delete item
    choice = input("Enter a task,\nEnter a number to remove.\nEnter 'e' for exit\n\n ")

    #for exit
    if choice == "e":
        exit()
  
    #for invalid choices
    if choice == "" or choice in todo:
        print("invalid")
        continue
  
    #test for add or delete
    #delete
    try:          
        for i in range(len(todo)): 
 
          if int(choice) == i:
              del_it(todo)
    #add
    except:
        add_it(todo)
        

        
          
        
