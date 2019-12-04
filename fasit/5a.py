def ring(ansattnummer, liste):
    while liste[ansattnummer] != -1:
        ansattnummer = liste[ansattnummer]
    return ansattnummer


print(ring(1, [2, -1, -1, 0]))
print(ring(3, [2, -1, -1, 0]))

#ny, riktig besvarelse
def gyldig(liste):
    for ansattnummer in liste:
        tall = ansattnummer
        while tall != -1:
            tall = liste[tall]
            if tall == ansattnummer:
                return False
    return True

print(gyldig([2, -1, -1, 0]))
print(gyldig([1, -1, 3, 4, 2]))
