from experta import *
import time

class Option(Fact):
    """Info about the COVID19"""
    pass

pointsCov = 0
pointsExtra = 0
older = 0

class Detector(KnowledgeEngine):

    #Count points depending on the answer
    def pointSystem(self, answer, typeQuestion):
        global pointsCov, pointsExtra, older
        if (answer == 'yes' and typeQuestion == 0):
            pointsCov = pointsCov + 1
            print(pointsCov)
            print(pointsExtra)
        else:
            if (answer == 'yes' and typeQuestion == 1):
                pointsExtra = pointsExtra + 1
                print(pointsCov)
                print(pointsExtra)
            else:
                if (answer == 'yes' and typeQuestion == 2):
                    older = 1
                    print(older)

    #Return global variables values
    def returnValues(self, typeValue):
        global pointsCov, pointsExtra, older
        if (typeValue == 0):
            return pointsCov
        else:
            if (typeValue == 1):
                return pointsExtra
            else:
                if (typeValue == 2):
                    return older

    #Reset global variables values
    def resetValues(self):
        global pointsCov, pointsExtra, older
        pointsCov = 0
        pointsExtra = 0 
        older = 0

    ######################################################
    ########## CORONAVIRUS MOST CASUAL SYMPTOMS ##########
    ######################################################

    @Rule("answer" << Option(q1=L("yes")
                    | L("no")))
    def first_question(self, answer):
        self.resetValues()
        self.pointSystem(answer["q1"], 0)
        #QUESTION 2
        self.declare(Option(q2=input("\nDo you feel short of breath? (that is not caused by a chronic or previously diagnosed disease)? \n[yes] [no]\nAnswer >> ").lower()))

    @Rule("answer" << Option(q2=L("yes")
                    | L("no")))
    def second_question(self, answer):
        self.pointSystem(answer["q2"], 0)
        #QUESTION 3
        self.declare(Option(q3=input("\nDo you have chest pain?? \n[yes] [no]\nAnswer >> ").lower()))

    @Rule("answer" << Option(q3=L("yes")
                    | L("no")))
    def third_question(self, answer):
        self.pointSystem(answer["q3"], 0)
        #QUESTION 4
        self.declare(Option(q4=input("\nDo you have a fever higher than 38°? \n[yes] [no]\nAnswer >> ").lower()))

    @Rule("answer" << Option(q4=L("yes")
                    | L("no")))
    def fourth_question(self, answer):
        self.pointSystem(answer["q4"], 0)
        #QUESTION 5
        self.declare(Option(q5=input("\nDo you have a persistent dry cough? \n[yes] [no]\nAnswer >> ").lower()))

    @Rule("answer" << Option(q5=L("yes")
                    | L("no")))
    def fifth_question(self, answer):
        self.pointSystem(answer["q5"], 0)
        #QUESTION 6
        self.declare(Option(q6=input("\nDo you have a runny nose? \n[yes] [no]\nAnswer >> ").lower()))

    @Rule("answer" << Option(q6=L("yes")
                    | L("no")))
    def sixth_question(self, answer):
        self.pointSystem(answer["q6"], 1)
        #QUESTION 7
        self.declare(Option(q7=input("\nDo you have a body aches or muscle pain? \n[yes] [no]\nAnswer >> ").lower()))

    @Rule("answer" << Option(q7=L("yes")
                    | L("no")))
    def seventh_question(self, answer):
        self.pointSystem(answer["q7"], 1)
        #QUESTION 8
        self.declare(Option(q8=input("\nDo you have sore throat? \n[yes] [no]\nAnswer >> ").lower()))

    @Rule("answer" << Option(q8=L("yes")
                    | L("no")))
    def eighth_question(self, answer):
        self.pointSystem(answer["q8"], 1)
        #QUESTION 9
        self.declare(Option(q9=input("\nDo you have diarrhea or stomach ache? \n[yes] [no]\nAnswer >> ").lower()))

    @Rule("answer" << Option(q9=L("yes")
                    | L("no")))
    def ninth_question(self, answer):
        self.pointSystem(answer["q9"], 1)
        #QUESTION 10
        self.declare(Option(q10=input("\nDid you receive/Are you getting medical treatment for your symptoms? \n[yes] [no]\nAnswer >> ").lower()))

    @Rule("answer" << Option(q10=L("yes")
                    | L("no")))
    def tenth_question(self, answer):
        self.pointSystem(answer["q10"], 1)
        #QUESTION 11
        self.declare(Option(q11=input("\nAre you older than 65 years? \n[yes] [no]\nAnswer >> ").lower()))

    @Rule("answer" << Option(q11=L("yes")
                    | L("no")))
    def eleventh_question(self, answer):
        self.pointSystem(answer["q11"], 2)
        #QUESTION 12
        self.declare(Option(duration=int(input("\nHow many days have you had those symptoms? \nAnswer >> "))))

    #COMPARATION
    @Rule(Option(duration =P(lambda x: (x >= 7))))
    def INDRE_quarentine(self):

        cov = self.returnValues(0)
        extra = self.returnValues(1)
        old = self.returnValues(2)

        print("\n\n")

        if cov >= 3:
            if old == 1:
                print("""It seems that you need more definitive health care services due to respiratory problems at the first moment, 
                         we will have to put you in extreme quarantine and we'll perform a COVID-19 test as fast as possible.""")
            else:
                print("""It seems that you need more definitive health care services due to respiratory problems at the first moment,
                         we will have to put you in quarantine and we'll perform a COVID-19 test when we can.
                         Stay calm, more than 80% of COVID-19 cases do not require hospitalization and recover at home.""")
        if cov < 3 and cov > 0:
            if old == 1:
                print("""It seems that you need more definitive health care services due to respiratory problems at the first moment,
                         we will have to put you in quarantine and we'll perform a COVID-19 test when we can.
                         Stay calm, more than 80% of COVID-19 cases do not require hospitalization and recover at home.""")
            else:
                print("""You are having some respiratory problems, but it's something that we can check at home,
                         try to stay safe at home and if your symptoms get worse, come back and we'll perform a test and take care of you.
                         Stay calm, more than 80% of COVID-19 cases do not require hospitalization and recover at home.""")
        if cov == 0 and extra > 3:
            if old == 1:
                print("""You have some symptoms of respiratory illness, but it is unlikely that it is COVID-19.
                         Please, stay at home and keep tracking of the symptoms, if they get worse, come back and we'll perform a test and take care of you.""")
            else:
                print("""You have some symptoms of respiratory illness, but it is unlikely that it is COVID-19.
                         Stay at home.""")
        if cov == 0 and (extra >= 0 and extra < 3):
            if old == 1:
                print("""You have some symptoms of respiratory illness, but it is unlikely that it is COVID-19.
                         Stay at home.""")
            else:
                print("""Just stay at home, 95% chance that you don't have COVID-19""")
        time.sleep(3)
        print("\n\n\n\n\n")

    @Rule(Option(duration =P(lambda x: x < 7)))
    def hospital_quarentine(self):

        cov = self.returnValues(0)
        extra = self.returnValues(1)
        old = self.returnValues(2)

        print("\n\n")

        if cov >= 3:
            if old == 1:
                print("""It seems that you need more definitive health care services due to respiratory problems at the first moment, 
                         we will have to put you in extreme quarantine and we'll perform a COVID-19 test as fast as possible.""")
            else:
                print("""You are having some respiratory problems, but it's something that we can check at home,
                         try to stay safe at home and if your symptoms get worse, come back and we'll perform a test and take care of you.
                         Stay calm, more than 80% of COVID-19 cases do not require hospitalization and recover at home.""")
        if cov < 3 and cov > 0:
            if old == 1:
                print("""You are having some respiratory problems, but it's something that we can check at home,
                         try to stay safe at home and if your symptoms get worse, come back and we'll perform a test and take care of you.
                         Stay calm, more than 80% of COVID-19 cases do not require hospitalization and recover at home.""")
            else:
                print("""You have some symptoms of respiratory illness and COVID-19 aswell, but it is unlikely that it is COVID-19.
                         Please, stay at home and keep tracking of the symptoms, if they get worse, come back and we'll perform a test and take care of you.""")
        if cov == 0 and extra > 3:
            if old == 1:
                print("""You have some symptoms of respiratory illness, but it is unlikely that it is COVID-19.
                         Please, stay at home and keep tracking of the symptoms, if they get worse, come back and we'll perform a test and take care of you.""")
            else:
                print("""You have some symptoms of respiratory illness, but it is unlikely that it is COVID-19.
                         Stay at home.""")
        if cov == 0 and (extra >= 0 and extra < 3):
            if old == 1:
                print("""You have some symptoms of respiratory illness, but it is unlikely that it is COVID-19.
                         Stay at home.""")
            else:
                print("""Just stay at home, 95% chance that you don't have COVID-19""")
        time.sleep(3)
        print("\n\n\n\n\n")
