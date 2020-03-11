# =================================================
# Title:  Assignment 07
# Description:  Exception Handling and Pickling
# changelog:
# David Wakazuru 03.05.20
# =================================================

import pickle


emp = {1: "A",2: "B",3:"C",4: "D"}
pickling_on = open("Emp.pickle", "wb")
pickle.dump(emp, pickling_on)
pickling_on.close()

file = open("emp.pickle", "rb")
list_of_data = pickle.load(file)
file.close()
print(emp)
print("This is collected and printed from a pickle\n")
print("Now we will exhibit an exception handling script\n")



def bitcoinConv():

    while True:
        try:
            number = int(input("How many bitcoins do you have? (First, try entering a word)\n"))
            print("You have $", + 8770 * number, "in btc")
            break
        except ValueError:
            print("Make sure you enter a number (this is exception handling).\n")


bitcoinConv()









