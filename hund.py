class Hund:
    #MAGISK konstruktør
    def __init__(self, navn, alder, rase=None):
        self._navn = navn
        self._alder = alder
        self._rase = rase

    #MAGISK stringmetode
    def __str__(self):
        if self._rase:
            return "Navn: " + self._navn + ", alder: " + str(self._alder) + ", rase: " + self._rase
        return "Navn: " + self._navn + ", alder: " + str(self._alder)

    #MAGISK erlikmetode
    def __eq__(self, annen):
        return self._alder == annen.hentAlder()

    #MAGISK større-enn-metode
    def __gt__(self, annen):
        return self._alder > annen.hentAlder()

    #MAGISK mindre-enn-metode
    def __lt__(self, annen):
        return self._alder < annen.hentAlder()

    def hentAlder(self):
        return self._alder

def hovedprogram():
    buster = Hund("Buster", 5)
    fido = Hund("Fido", 20, "Dacschschs")
    print(fido)
    print(buster)

    if fido == buster:
        print("Hundene er like gamle")
    elif fido < buster:
        print("Fido er yngre enn Buster")
    else:
        print("Buster er yngre enn Fido")

hovedprogram()
