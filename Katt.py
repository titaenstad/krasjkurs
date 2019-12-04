class Katt:

    def __init__(self, navn, alder, farge):
        self._navn = navn
        self._alder = alder
        self._farge = farge

    def hentAlder(self):
        return self._alder

    def hentNavn(self):
        return self._navn

    def hentFarge(self):
        return self._farge

    #Frivillig
    def __str__(self):
        return "Navn: " + self._navn + ", Alder: " + str(self._alder) + ", Farge: " + self._farge