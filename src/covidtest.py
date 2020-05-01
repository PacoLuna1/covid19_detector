# coding=utf-8
#!/usr/bin/python
from  src.__init__ import Detector, Option, APICOVID

class CovidTest():

    def __init__(self):
        self.name = "CovidTest"
        self.apicovid = APICOVID()

    def menu(self):
        stay = True
        invalidValue = "--> Please enter a valid value"
        opt1 = "1. Start test"
        opt2 = "2. Information about the Coronavirus"
        opt3 = "0. Exit"
        line = "\n"

        while(stay):
            print("==== Welcome to the Corona Virus Detector ===")
            print("Please choose a valid option: ")
            print(opt1 + line + opt2 + line + opt3)
            print("============================================")
            try:
                opt = int(input())

                if(opt == 1):
                    self.startEngine()
                elif(opt == 2):
                    self.consultInfo(invalidValue)
                elif(opt == 0):
                    print("finish")
                    stay = False
                else:
                    print(invalidValue)
            except:
                print(invalidValue)

    def startEngine(self):
        engine = Detector()
        engine.reset()
        print("Test to know if the user is infected with Covid-19")
        engine.declare(Option(symptom=input("Which is your first symptom? : ")))
        engine.run()

    def consultInfo(self, invalidValue):
        stay = True
        while(stay):
            try:
                country = input("Please capture the name of the country: ")
                stay = False
                self.apicovid.getInfo(country)
            except:
                print(invalidValue)
