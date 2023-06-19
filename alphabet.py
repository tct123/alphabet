def rueckwaertz(letters):
    liste = []
    lett = len(letters)
    for letter in letters:
        liste.append(letter)
    print(liste)
    listerueck = []
    print(lett)
    for letter in liste:
    	listerueck.append(liste[lett])
    	lett = lett-1
    print(listerueck)
letters = "abcdefghijklmnopqrstuvwxyz"
rueckwaertz(letters=letters)
