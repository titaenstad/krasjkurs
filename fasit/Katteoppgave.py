# Del 1

navn = "Jens"
alder = 3
farge = "rød"

if farge == "rød":
    if alder > 5:
        print("Hurra,", navn, "ble adoptert!")
    else:
        print("Olga vil holde et øye med", navn)

#evt
if alder > 5 and farge == "rød":
    print("Hurra,", navn, "ble adoptert!")
elif farge == "rød":
    print("Olga vil holde et øye med", navn)


# Del 2

olgas_katter = []

def sjekkKatt(navn, alder, farge):
    if farge == "rød":
        if alder > 5:
            print("Hurra,", navn, "ble adoptert!")
            olgas_katter.append(navn)
        else:
            print("Olga vil holde et øye med", navn)

def testSjekkKatt():
    sjekkKatt("Boris", 5, "svart")
    sjekkKatt("Leo", 7, "rød")
    sjekkKatt("Pusur", 0.5, "rød")
    sjekkKatt("Snuten", 10, "grå")
    print(olgas_katter)

testSjekkKatt()


# Del 3
from Kattehjem import Kattehjem
from Katt import Katt

olgas_katter = []
katzenjammer = Kattehjem()

def sjekkKatt(katt):
    if katt.hentFarge() == "rød":
        if katt.hentAlder() > 5:
            print("Hurra,", katt.hentNavn(), "ble adoptert!")
            katzenjammer.flyttUtKatt(katt)
            olgas_katter.append(katt)
        else:
            print("Olga vil holde et øye med", katt.hentNavn())

def sjekkKatzenjammer():
    for katt in katzenjammer.hentKatter():
        sjekkKatt(katt)

def lesFilOgFlyttInn():
    fil = open("katz.txt")
    for linje in fil:
        biter = linje.split(", ")
        katt = Katt(biter[0], float(biter[1]), biter[2].strip())
        katzenjammer.flyttInnKatt(katt)
    fil.close()

lesFilOgFlyttInn()
sjekkKatzenjammer()
print(olgas_katter)