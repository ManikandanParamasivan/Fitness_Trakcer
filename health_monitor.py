import datetime
def time():
    return datetime.datetime.now()

def addinfo(a):
    if a == 1:
        c = int(input("Choose the operation\n 1. Diet\n 2. Exercise\n"))
        if c == 1:

            print("Your are going to add Mani Diet file\n")
            v = input("Type the info : \n")
            with open("Mani_Diet.txt", "a") as op:
                op.write(str([str(time())]) +": " + v + "\n")
                print("Successfully added !!")

        elif c == 2:
            print("Your are going to add Mani Excercise file\n")
            v = input("Type the info : \n")
            with open("Mani_Exercise.txt", "a") as op:
                op.write(str([str(time())]) + ": " + v + "\n")
                print("Successfully added !!")

    elif a == 2:
        c = int(input("Choose the operation\n 1. Diet\n 2. Exercise\n"))
        if c == 1:
            print("Your are going to add Ryu Diet file")
            v = input("Type the info : ")
            with open("Ryu_Diet.txt", "a") as op:
                op.write(str([str(time())]) + ": " + v + "\n")
                print("Successfully added !!")

        elif c == 2:
            print("Your are going to add Ryu Exercise file\n")
            v = input("Type the info : \n")
            with open("Exercise_Ryu.txt", "a") as op:
                op.write(str([str(time())]) + ": " + v + "\n")
                print("Successfully added !!")



def retinfo(b):
    if b == 1:
        print("You are inside the client - Mani\n")
        a = int(input("Choose what you want to view\n 1. Diet \n 2. Exercise\n"))
        if a == 1:
            with open("Mani_Diet.txt") as op:
                for i in op:
                    print(i, end="")

        elif a == 2:
            with open("Mani_Exercise.txt") as op:
                for i in op:
                    print(i, end="")

    elif b == 2:
        print("You are inside the client - Ryu\n")
        a = int(input("Choose what you want to view\n 1. Diet \n 2. Exercise\n"))
        if a == 1:
            with open("Ryu_Diet.txt") as op:
                for i in op:
                    print(i, end="")

        elif a == 2:
            with open("Exercise_Ryu.txt") as op:
                for i in op:
                    print(i, end="")





print("****** Welcome to Raven Health Monitor ******")
print("| Select the operation |\n 1. Add\n 2. Retrieve\n")
client = int(input())
if client == 1 :
    add = int(input("Choose the client\n 1. Mani\n 2. Ryu\n"))
    addinfo(add)
elif client == 2:
    ret = int(input("Choose the client\n 1. Mani\n 2. Ryu\n"))
    retinfo(ret)
