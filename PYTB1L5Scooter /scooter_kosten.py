import time

print("Calculatie voor hoeveel je spendeerd aan je maandlasten...")
def bereken_maandkosten(km):
    km_per_maand = km
    liter_per_kilometer = 0.4
    benzine_kosten_per_liter = 1.94
    verzekering_per_maand = 38
    maandkosten = km_per_maand * liter_per_kilometer * benzine_kosten_per_liter + verzekering_per_maand
    time.sleep(1.2)
    print(".....calulating......")
    time.sleep(2)
    return maandkosten

print(bereken_maandkosten(int(input("Hoeveel KM rij je pm? "))))
