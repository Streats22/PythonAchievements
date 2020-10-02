naam = input("Wat is je naam?" )
leeftijd = input(naam + "Hoe oud ben je?" )
Woonplaats = input(naam + "Waar kom je vandaan?" )
print("Kies graag uit een van deze B (broers) Z (Zussen) G (geen)")

keuze = input()
if keuze == "B":
    print(" Hoeveel broers heb je? ")
    Antaalbroers = input()
    print("naam: ", naam, "leeftijd :", leeftijd, "Woonplaats:",Woonplaats, "Aantal Broers:", Antaalbroers )

elif keuze == "Z":
    print(" Hoeveel Zussen heb je? ")
    AantalZussen = input()
    print("naam: ", naam, " leeftijd :", leeftijd, "Woonplaats:", "Aantal Zussen:", AantalZussen )

elif keuze == "G":
    print("naam: ", naam, " leeftijd :", leeftijd, "Woonplaats:", Woonplaats, "veder geen broers of zussen")

else :
    print(naam + " Voer graag een van de 3 keuzes in :)")
