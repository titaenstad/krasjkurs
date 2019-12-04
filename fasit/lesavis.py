fil = open("avis.txt")

komplementer = []

for linje in fil:
    if linje[0].isdigit():
        komplementer.append(linje)

fil.close()
fil = open("Komplementer.txt", "w+")

for komplement in komplementer:
    fil.write(komplement)

fil.close()