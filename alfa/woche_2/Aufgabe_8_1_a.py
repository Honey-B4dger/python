#
# Aufgabe 8a
#
def ask_name():
    myDict ={}
    active = True
    while active:
        name=""
        age=""
        while not name.isalpha():  # ask as long as no alphabetic input 
            name = input("What is your name? ")
        while not age.isnumeric(): # ask as long as no numeric input
            age = input("What is your age? ")
        myDict[name] = int(age)
        res = input("Continuing, Abort with \"n\" ")
        if res == "n":
            active = False
#    elif res != "n": 
#        print("elif loop" + str(myDict))
#    else:   
 #       print("else loop" + str(myDict))
    return myDict

myDict = ask_name()
print("Names entered are:")
print(myDict)