#!/usr/bin/env python

db = {}         

def newuser():
    prompt = "login desired: "
    while True:
        name = raw_input(prompt)
        if db.has_key(name):
            prompt = "name taken,try another: "
            continue
        else:
            break
    while True:                                 #checkout the password
        pwd1 = raw_input("please enter your passwd: ")
        pwd2 = raw_input("please enter your passwd again: ")
        if(pwd1 != pwd2):
            print "The password is different"
            continue
        else:
            break

    db[name] = pwd1
    print "welcome to the page!"


def olduser():
    name = raw_input("login: ")
    if name not in db:
        print "Error !No user name!"
        return False
    pwd = raw_input("passwd: ")
    passwd = db.get(name)
    if passwd == pwd:
        print "welcome back ",name
    else:
        print "login incorrect"



def showmenu():
    prompt="""
            (N)ew User login
            (E)xisting User login
            (Q)uit

            Enter choice: """
    
    while True:

        chosen = False
        while not chosen:
            try:
                choice = raw_input(prompt).strip()[0].lower()
    
            except( EOFError , KeyboardInterrupt):
                choice = "q"
            print "\nYou picked: [%s]" % choice
            if choice not in "neq":
                print "Invalid option , try again"
            else:
                chosen = True

        if choice == "q":
            break
        if choice == "n":
            newuser()
        if choice == "e":
            olduser()


if __name__ == "__main__":
    showmenu()


