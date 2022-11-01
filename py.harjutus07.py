#J.M.O
#01.11.2022
#harjutus07
import math

#programm
def kuup(a):
    print(f"Kuubi ruumala on {a**3}")

def kera(j):
    print(f"Kera ruumala on {round(4/3*math.pi*(j**2),2)}")


def koonus(a,h):
    print(f"Koonuse ruumala on {round((math.pi*a**2)*h/3,2)}")

def silinder(r,h):
    print(f"Silindri ruumala on {math.pi*(r**2)*h}") 

print("************** LEIAME RUUMALA **************")
loop = 1

while loop==1:
    print("Vali kujund: \n1.Kuup \n2.Kera \n3.Koonus \n4.Silinder")
    kujund = int(input("Lisa kujundi number 1-4: "))
    if kujund==1:
        x = int(input("Sisesta kuubi külje pikkus: "))
        kuup(x)
    elif kujund==2:
        k = int(input("Sisesta kera raadius"))
        kera(k)
    elif kujund==3:
        r = int(input("Sisesta koonuse põhja raadius: "))
        h = int(input("Sisesta koonuse kõrgus: "))
        koonus(r,h)
    elif kujund==4:
        r = int(input("Sisesta silndri raadius: "))
        h = int(input("Sisetsa slindri kõrgus: "))
        silinder(r,h)
    else:
        print("**************\nPalun tee valik 1-4\n**************")









#oma funktsiooni loomine
def tervita(a="unknown", b="ge"):
    if b=="et":
        print(f"Tere {a}")
    elif b=="en":
        print(f"Hi {a}")
    else:
        print(f"Hallo {a}")
#funktsiooni väljakutsumine
tervita("jan","et")