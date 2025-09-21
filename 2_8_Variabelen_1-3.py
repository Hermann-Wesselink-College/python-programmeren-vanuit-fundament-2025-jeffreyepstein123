prijs = 24.49
print('Prijs: ' + str(prijs))

voornaam = 'Sjaak'
achternaam = 'Heuvels'
print('Mijn naam is ' + voornaam + ' ' + achternaam)
print('Mijn naam bestaat uit ' + str(len(voornaam + ' ' + achternaam)) + ' letters')
print(voornaam.lower())
print(achternaam.upper())

voornaam = input("Wat is je voornaam? ")
achternaam = input("Wat is je achternaam? ")

naam = voornaam + " " + achternaam

print("Je naam is: " + naam)
print("Je naam bestaat uit " + str(len(naam)) + " letters (inclusief spaties)")