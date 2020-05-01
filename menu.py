from detector import *

class Menu():
    stay = True
    while(stay):
        print("==== Welcome to the Corona Virus Detector ===")
        print("Please choose a valid option: ")
        print("1. Start test")
        print("2. Information about the Coronavirus Cases in México")
        print("3. Exit")
        print("============================================")
        opt = int(input())
        if(opt == 1):
            start = TestStart()
            start.startEngine()
        elif(opt == 2):
            print("something")
        elif(opt == 3):
            print("finish")
            stay = False
        else:
            print("--> Please enter a valid value")