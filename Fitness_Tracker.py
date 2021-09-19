"""
PERSONAL FITNESS TRACKER
CREATOR : - RYUJIN SAMA
DISCRIP :- SIMPLE PYTHON BASED PROECT TO STORE DAILY FITNESS ACTIVITY,DIET, WEIGHT
CHANGES UPCOMING ;- DATA VISUALIZATION TO SHOW THE PERFORMANCE OF THE USER THROUGHOUT THE WEEK/MONTH/YEAR

"""





import datetime

def time():
    return datetime.datetime.now()

def adddata(b):
    if b == 1:
        food = input()
        food = food.lower()
        if food == "roti":
            calorie = "534"
            with open("DIET_OF_USER.txt","a") as dt:
                dt.write(str([str(time())]) + ": " + food + " : " + calorie + "\n" )
            print("-------------------------------------------------------")
            print("|                 ADDED SUCCESSFULLY                  |")
            print("|                  KEEP WORKING !!!                   |")
            print("-------------------------------------------------------")
        elif food == "rice":
            calorie = "564"
            with open("DIET_OF_USER.txt","a") as dt:
                dt.write(str([str(time())]) + ": " + food + " : " + calorie+ "\n" )
            print("-------------------------------------------------------")
            print("|                 ADDED SUCCESSFULLY                  |")
            print("|                  KEEP WORKING !!!                   |")
            print("-------------------------------------------------------")

        elif food == "idli":
            calorie = "304"
            with open("DIET_OF_USER.txt","a") as dt:
                dt.write(str([str(time())]) + ": " + food + " : " + calorie+ "\n" )
            print("-------------------------------------------------------")
            print("|                 ADDED SUCCESSFULLY                  |")
            print("|                  KEEP WORKING !!!                   |")
            print("-------------------------------------------------------")

        elif food == "dosa":
            calorie = "634"
            with open("DIET_OF_USER.txt","a") as dt:
                dt.write(str([str(time())]) + ": " + food + " : " + calorie+ "\n" )
            print("-------------------------------------------------------")
            print("|                 ADDED SUCCESSFULLY                  |")
            print("|                  KEEP WORKING !!!                   |")
            print("-------------------------------------------------------")

        else:
            calorie = (input("Enter the Calorie value :"))
            with open("DIET_OF_USER.txt","a") as dt:
                dt.write(str([str(time())]) + ": " + food + " : " + calorie + "\n" )
            print("-------------------------------------------------------")
            print("|                 ADDED SUCCESSFULLY                  |")
            print("|                  KEEP WORKING !!!                   |")
            print("-------------------------------------------------------")

    elif b == 2:
        excer = input()
        excer = excer.lower()
        if excer == "skipping":
            t = int(input("How many minutes do you skip : "))
            t1 = 13 * t
            with open("EXERCISE_USER.txt", "a") as ex:
                ex.write(str([str(time())]) + ":" + str(excer) + " for " + str(t) + " minutes and burned" + str(t1) + "calories\n")
            print("-------------------------------------------------------")
            print("|                 ADDED SUCCESSFULLY                  |")
            print("|                  KEEP WORKING !!!                   |")
            print("-------------------------------------------------------")

        elif excer == "running":
            t = int(input("How many minutes do you run : "))
            t1 = 11.7 * t
            with open("EXERCISE_USER.txt", "a") as ex:
                ex.write(str([str(time())]) + ":" + str(excer) + " for " + str(t) + " minutes and burned" + str(t1) + "calories\n")
            print("-------------------------------------------------------")
            print("|                 ADDED SUCCESSFULLY                  |")
            print("|                  KEEP WORKING !!!                   |")
            print("-------------------------------------------------------")

        elif excer == "football":
            t = int(input("How many minutes do you play : "))
            t1 = 8.95 * t
            with open("EXERCISE_USER.txt", "a") as ex:
                ex.write(str([str(time())]) + ":" + str(excer) + " for " + str(t) + " minutes and burned" + str(t1) + "calories\n")
            print("-------------------------------------------------------")
            print("|                 ADDED SUCCESSFULLY                  |")
            print("|                  KEEP WORKING !!!                   |")
            print("-------------------------------------------------------")

        else:
            t = int(input("How many minutes do you workout : "))
            t1 = int(input("How many calories burned total : "))
            with open("EXERCISE_USER.txt", "a") as ex:
                ex.write(str([str(time())]) + ":" + str(excer) + " for " + str(t) + " minutes and burned" + str(t1) + "calories\n")
            print("-------------------------------------------------------")
            print("|                 ADDED SUCCESSFULLY                  |")
            print("|                  KEEP WORKING !!!                   |")
            print("-------------------------------------------------------")

    elif b == 3:
        wiegh = int(input("Enter the new weight : "))
        with open("WEIGH_USER.txt", "a") as wu:
            wu.write(str([str.time()]) + " USER WEIGHT IS " + wiegh + "\n")
            print("-------------------------------------------------------")
            print("|                 ADDED SUCCESSFULLY                  |")
            print("|                  KEEP WORKING !!!                   |")
            print("-------------------------------------------------------")


def viewdata(c):
    if c == 1:
        with open("DIET_OF_USER.txt") as du:
            for i in du:
                print(i, end ="")

    elif c == 2:
        with open("EXERCISE_USER.txt") as eu:
            for i in eu:
                print(i, end ="")
    elif c == 3:
        with open("WEIGH_USER.txt") as wu:
            for i in wu:
                print(i, end="")



print("-------------------------------------------------------")
print("|          WELCOME TO RAVEN FITNESS TRACKER           |")
print("|    Glad to meet you & Thank you for choosing us!    |")
print("|             Press any key to continue               |")
print("-------------------------------------------------------")
init = input()

print("-------------------------------------------------------")
print("|              CHOOSE YOUR OPERATION                  |")
print("| 1. To Add Data                                      |")
print("| 2. To View Data                                     |")
print("| 3. To Exit                                          |")
print("-------------------------------------------------------")

a = 0
while a != 3 :
    a = int(input())
    if a == 1:
        print("-------------------------------------------------------")
        print("|             YOU SELECTED TO ADD DATA                |")
        print("|               SELECT THE OPERATION                  |")
        print("| 1. DIET                                             |")
        print("| 2. EXERCISE                                         |")
        print("| 3. NEW/EDIT WEIGHT                                  |")
        print("| 4. EXIT                                             |")
        print("-------------------------------------------------------")
        b = int(input())
        if b == 4:
            break
        else:
            adddata(b)
    elif a == 2:
        print("-------------------------------------------------------")
        print("|             YOU SELECTED TO VIEW DATA               |")
        print("|               SELECT THE OPERATION                  |")
        print("| 1. DIET                                             |")
        print("| 2. EXERCISE                                         |")
        print("| 3. PERFORMANCE                                      |")     #this is not yet started to work.
        print("| 4. EXIT                                             |")
        print("-------------------------------------------------------")
        c = int(input())
        if c == 4:
            break

        else:
            viewdata(c)

