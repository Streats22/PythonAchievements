##Om Functies te oefenne heb ik alle sommen in een fuctie gezet :)
#De laatste 2 zijn alleen met een Var gedaan.
def Optellen(varA, varB):
    print("Optellen", varA + varB)

Optellen(50, 20)

def Aftrekken(varA, varB):
    print("Aftrekken",varA - varB)
Aftrekken(500, 70)


def Delen(varA, varB):
    print("Delen",varA / varB)
Delen(250, 2)

def Keer(varA, varB):
    print("Modulo/RestWaarde",varA * varB)
Keer(2, 53)

def RestW(varA, varB):
    print("Modulo/RestWaarde",varA % varB)

RestW(25, 20)

def Vloerdevisie(varA, varB):
    print("Vloerdevisie",varA / varB)

Vloerdevisie(21,432)

def EXPONENT(varA, varB):
    print("EXPONENT",varA ** varB)

EXPONENT(42,11)


F = 2
F += 2
print("Optellen bij Waarde",F)


F /= 2
print("Delen Door Waarde",F)

F -= 2
print("Min Waarde",F)

F *= 2
print("Keer Waarde",F)
