#J.M.O
#14.11.22
#iseseisev töö




#peo eelarve
kutsutud = int(input("Mitu kutsutud: "))
tuleb = int(input("Mitu tuleb: "))
eelarve = 55

print(kutsutud*eelarve)


#tervitused




#Õunamahla tegemine

ounad = int(input("Õunte kogus (kg): "))
mahlapakke = round(ounad * 0.4 / 3,)
print(mahlapakke)



#bänner
def banner(c):
    c = c.upper()
    return c

c = int(input("Mitu korda soovite reklaamilauset kuvada"))
f = input("Mida soovite kuvada? ")
for i in range(c):
    print(f.upper())
   





#ounad
import random
mitu = int(input("Mitu pöialpoissi tahab õunu?: "))

ounad = 0
for i in range(mitu):
    suv=random.randint(1,2)
    ounad+=suv
    print(suv)
print(f"Alles jäi {12-ounad} õuna")

#murelikud lapsevanemad
mehis = int(input("pls ring arv: "))
ring = 0
porgand = 0
while ring<mehis:
    ring +=1
    if ring%2==0:
        porgand+=ring
print(f"porgand: {porgand}")

#äratus
aratus = int(input("Mitu korda äratada: "))
for i in range(aratus):
    print("Tõuse ja sära!")

#bussid
import math

inimeste_arv = int(input("inimeste arv: "))
kohtade_arv = int(input("kohtade arv: "))
bussid = math.ceil(inimeste_arv/kohtade_arv)
print(f"Busse vaja: {bussid}")
inimesed = inimeste_arv%kohtade_arv
if inimesed==0:
    print(f"viimases bussis: {kohtade_arv}")
else:
    print(f"viimases bussis: {inimesed}")






#aasta liblikas
aasta = 2020
liblikas = "teelehe-mosaiikliblikas"
lause_keskosa = ". aasta liblikas on "
lause = str(aasta)+lause_keskosa+liblikas

print(lause)
#tervitus
print("Tere, maailm!")
