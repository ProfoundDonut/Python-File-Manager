""" Hayden's Shit
#What is this going to be about?
def loop():
    print("Authorized user...")
    print("...")
    print("Loading PyShell...")
    print("...")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("Welcome to PyShell!")
    lup = True
    while loop == True:
        var = input(name + "--$> ")
        if var == "help"

        else:
            print("That is not a command. Please type 'help' for help.")
name = input("What is your name? \n")
if name.lower() == "hayden" or name.lower() == "max" or name.lower() == "hunter":
    loop()
"""
import csv
import os
import sys

usr_dat = ".usr_dat"
new_usr_var = "NewUser"
new_pas = "Admin12"
term_prompt = "$"

path = ".term"
if os.path.exists(path) and os.path.isdir(path):
    print("Terminal path loaded.")
else:
    print("Terminal path not foud, creating terminal path.")
    os.mkdir(path)
    print("Terminal path loaded.")
os.chdir(path)

def write(x,y):
    with open(x, 'w') as csvfile:
        writer = csv.writer(csvfile)
        [writer.writerow(r) for r in sorted(y)]

def read(x):
    with open(x, 'r') as csvfile:
        reader = csv.reader(csvfile)
        table = [[str(e) for e in r] for r in reader]
    return table

def login(x,y,usr_dat,new_usr_var,new_pas):
    try:
        read(usr_dat)
    except:
        write(usr_dat,[[new_usr_var,new_pas]])
    usr_dat = read(usr_dat)
    for i in range(len(usr_dat)):
        if usr_dat[i][0] == x and usr_dat[i][1] == y:
            return x
    return "nil"

def new_usr(usr_dat,new_usr_var,new_pas):
    try:
        read(usr_dat)
    except:
        write(usr_dat,[[new_usr_var,new_pas]])
    done = False
    while not done:
        table = read(usr_dat)
        usr = input("Enter New Username: ")
        found = False
        for i in range(len(table)):
            if table[i][0] == usr:
                found = True
        if not found:
            done1 = False
            while not done1:
                pas = input("Enter New Password: ")
                check_pas = input("Confirm New Password: ")
                if pas == check_pas:
                    table = table + [[usr,pas]]
                    write(".usr_dat", table)
                    print("New User Created!")
                    done1 = True
                    done = True
                else:
                    print("Password not consistant.")
        else:
            print("That user alredy exsists.")


is_logged_in = False
while not is_logged_in:
    usr = login(input("Enter Username: "), input("Enter Password: "), usr_dat,new_usr_var,new_pas)
    if usr == "nil":
        print("Invalid username or password.")
    elif usr == new_usr_var:
        new_usr(usr_dat,new_usr_var,new_pas)
    else:
        is_logged_in = True


path = "." + usr + "_dat"
if os.path.exists(path) and os.path.isdir(path):
    print("User path loaded.")
else:
    print("User path not foud, creating user path.")
    os.mkdir(path)
    print("User path loaded.")
os.chdir(path)

exit = False
while not exit:
    command = input(usr + term_prompt)
    if command != "":
        if os.path.exists(command + ".py"):
            os.system("python3 " + command + ".py")
        elif command == "exit":
            os._exit(1)
        elif command[:4] == "edit":
            if os.path.exists(command[5:] + ".py"):
                os.system("open -a Atom.app"+command[5:]+".py")
            else:
                open(command[5:]+".py", 'w').close()
                os.system("open -a Atom.app "+command[5:]+".py")
