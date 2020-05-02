# coding=utf-8
#!/usr/bin/python
from  src.__init__ import Detector, Option, APICOVID
import time
import os

class CovidTest():

    def __init__(self):
        self.name = "CovidTest"
        self.apicovid = APICOVID()

    def startEngine(self):
        engine = Detector()
        engine.reset()
        print("Test to know if the user is infected with Covid-19\n")
        #QUESTION 1
        question = str(input("Have you had direct contact with any covid-19 positive case? \n[yes] [no]\nAnswer >> ").lower())
        if (question != 'yes' and question != 'no'):
            print("I apologize, I don't understand.\nReturning to the menu...")
            time.sleep(1)
            print("\n\n\n\n\n")
            pass
        engine.declare(Option(q1 = question))
        engine.run()
        
    def menu(self):
        stay = True
        while(stay):
            print("\n==== Welcome to the Corona Virus Detector ===\n")
            print("Please choose a valid option: ")
            print("1. Start test")
            print("2. Information about the Coronavirus Cases in México")
            print("3. Exit")
            self.apicovid.getInfo("Mexico")
            print("============================================")
            opt = int(input(">>> "))
            if(opt == 1):
                self.startEngine()
            elif(opt == 2):
                print("something")
            elif(opt == 3):
                print("See you later!")
                stay = False
            else:
                print("--> Please enter a valid value")
