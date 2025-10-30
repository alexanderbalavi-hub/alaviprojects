class GCD:
    def __init__(self): # Konstruktor, initialisiert die Klasse
        self.result = 0
    def gcd(self, smaller, larger): # Methode, erste Funktion der Klasse
        larger = larger - smaller
        if smaller > larger: 
            self.gcd(larger, smaller)  # Rekursiver Aufruf der Methode
        elif smaller != larger:
            self.gcd(smaller, larger) # Rekursiver Aufruf der Methode
        else:
            self.result = larger  # Ergebnis speichern      

gcd_class = GCD()
smaller = 65
larger = 143
gcd_class.gcd(smaller, larger)
print("gcd(%s, %s) = %s" % (smaller, larger, gcd_class.result))
