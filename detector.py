from experta import *

class TestStart():
    def startEngine(self):
        engine = coronavirusDetector()
        engine.reset()
        print("Test to know if the user is infected with Covid-19")
        engine.declare(Option(symptom=input("Which is your first symptom?")))
        engine.run()

class Option(Fact):
    pass

class coronavirusDetector(KnowledgeEngine):

    @Rule(Option(symptom=L("tos seca")
                       | L("dolor de cabeza")))
    def second_symptom(self):
        self.declare(Option(symptom2=input("Which is your second symptom?")))

    @Rule(Option(symptom2=L("dolor de cabeza")
                        | L("tos seca")))
    def another_symptom(self):
        print("Disnea, Artralgias, Nealgias, Ordinofagia, Rinorrea, Conjuntivitis, Dolor Torasico")
        self.declare(Option(symptom3=input("What other symptom do you have?")))
        
        
    @Rule(Option(symptom3=L("disnea")
                        | L("artralgias")
                        | L("nealgias")
                        | L("odinofagia")
                        | L("rinorrea")
                        | L("conjuntivitis")
                        | L("dolor torasico")))
    def symptops_duration(self):
        self.declare(Option(duration=int(input("How long have you had symptoms?"))))

    @Rule(Option(duration =P(lambda x: x >= 7)))
    def INDRE_quarentine(self):
        print("You are going to be quarantined at the hospital and we will send your test to the INDRE(Instituto de Diagnóstico y Referencia Epidemiológicos)")

    @Rule(Option(duration =P(lambda x: x < 7)))
    def hospital_quarentine(self):
        print("You are going to be quarantined at your house")