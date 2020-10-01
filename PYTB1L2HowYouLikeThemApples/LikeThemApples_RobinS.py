import math
AppleBomen = 333
ShadowToSun = 333 / 3
ShadowToSun_apples = 146 / 100 * 80
#print(ShadowToSun_apples)

#print(ShadowToSun)

BomenInSchaduw = math.ceil(222)
ApplebomenInZon = 111

ApplebomenZon_Apples = 146
ApplesBomenShadow_Apples = 116.8

Appeles_Zon = ApplebomenInZon * ApplebomenZon_Apples
Appels_Shadow = BomenInSchaduw * ApplesBomenShadow_Apples
TotaalAppels = Appeles_Zon + Appels_Shadow
#print("Totaal aantal Appels",TotaalAppels)

Vrienden = 3
ApplesPP = TotaalAppels // Vrienden
#print("Er zijn ",ApplesPP, " Per persoon")

ApplesTeEten = 1
TeVerkopenApples = ApplesPP - ApplesTeEten

Verkoop = TeVerkopenApples
print("We eten :",ApplesTeEten, "apple('s)")
print("Ik verkoop: ",Verkoop, "Apple('s) ")
