class MyClass: 
    def __init__(self): #Konstruktor, initialisiert die Klasse
        self.alter = 38
    def getAlter(self,arg1): # Methode, erste Funktion der Klasse    
        print("arg1 =", arg1)
        return self.alter + arg1

my_Obj = MyClass() #Objekt der Klasse erstellen
result = my_Obj.getAlter(2) # Methode der Klasse aufrufen
print("Result =", result)    # Ausgabe des Resultats