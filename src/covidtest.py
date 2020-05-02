# coding=utf-8
#!/usr/bin/python
from  src.__init__ import *

class CovidTest():

    def __init__(self):
        self.name = "CovidTest"
        self.apicovid = APICOVID()
        self.globalStats = self.apicovid.getGlobalStats()


    def cleanScreen(self):
        os.system('clear')

    def enterToContinue(self):
        input(line + "Enter to continue...")
        print(line)

    def menu(self):
        stay = True
        invalidValue = red + "--> Please enter a valid value ✗" + RESET + line
        validValue = green + "--> Valid value ✓" + RESET + line
        opt1 = "1. Start test"
        opt2 = "2. Information about the Coronavirus"
        opt3 = "3. Worldwide cases"
        opt0 = "0. Exit"
        byebye= "See you soon! Stay at home, stay healthy! ❤️ "

        while(stay):
            print(yellow + "==== Welcome to the Corona Virus Detector ===" + RESET)
            print(opt0 + line+ opt1 + line + opt2 + line + opt3)
            print(yellow + "============================================" + RESET)
            try:
                opt = int(input("Select an option: "))
                if(opt == 1):
                    print(validValue)
                    self.startEngine()
                elif(opt == 2):
                    print(validValue)
                    self.consultInfo(invalidValue)
                elif(opt == 3):
                    print(validValue)
                    self.consultWorldWide()
                elif(opt == 0):
                    print(validValue + byebye)
                    stay = False
                    self.enterToContinue()
                else:
                    print(invalidValue)
            except:
                print(invalidValue)
                self.enterToContinue()
                self.cleanScreen()

    def startEngine(self):
        engine = Detector()
        engine.reset()
        print("Test to know if the user is infected with Covid-19\n")
        #QUESTION 1
        question = str(input("Have you had direct contact with any covid-19 positive case? \n[yes] [no]\nAnswer >> ").lower())
        if (question != 'yes' and question != 'no'):
            print("I apologize, I don't understand.\nReturning to the menu...")
            time.sleep(1)
            self.cleanScreen()
            pass
        engine.declare(Option(q1 = question))
        engine.run()

    def consultInfo(self, invalidValue):
        stay = True
        while(stay):
            try:
                country = input("Please capture the name of the country: ")
                stay = False
                self.apicovid.getInfo(country)
                input("Enter to continue...")
            except:
                print(invalidValue)
        self.cleanScreen()

    def consultWorldWide(self):
        print(yellow + "============================================" + RESET)
        print(cyan + "Worldwide cases: " + RESET + str(self.globalStats['TotalCases']))
        print(cyan +"Worldwide deaths: " + RESET + str(self.globalStats['GlobalDeaths']))
        print(cyan +"Worldwide recoverements: " + RESET + str(self.globalStats['GlobalRecovered']))
        print(yellow + "============================================" + RESET)
        self.enterToContinue()
        self.cleanScreen()
