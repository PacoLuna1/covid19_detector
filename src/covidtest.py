# coding=utf-8
#!/usr/bin/python
from  src.__init__ import Detector, Option, APICOVID

class CovidTest():

    def __init__(self):
        self.name = "CovidTest"
        self.apicovid = APICOVID()

    def startEngine(self):
        engine = Detector()
        engine.reset()
        print("Test to know if the user is infected with Covid-19")
        engine.declare(Option(symptom=input("Which is your first symptom?")))
        engine.run()

    def menu(self):
        stay = True
        while(stay):
            print("==== Welcome to the Corona Virus Detector ===")
            print("Please choose a valid option: ")
            print("1. Start test")
            print("2. Information about the Coronavirus Cases in México")
            print("3. Exit")
            self.apicovid.getInfo("Mexico")
            print("============================================")
            opt = int(input())
            if(opt == 1):
                self.startEngine()
            elif(opt == 2):
                print("something")
            elif(opt == 3):
                print("finish")
                stay = False
            else:
                print("--> Please enter a valid value")
