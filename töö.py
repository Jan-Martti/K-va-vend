#J.M.O
#09/11.22
#jaga mulle ekraani palun

import random
import math

#
fail = open("rebased.txt", encoding="UTF-8")

vastuvoetud = [2011,2012,2013,2014,2015,2016,2017,2018,2019]
aastad = []
for rida in fail:
    vastuvoetud.append(int(rida))
aasta = int(input("Mis aastat vaja?: "))
index = aastad.index(vastuvoetud)
print(index)
    
    
    
    
    

print(vastuvoetud)

fail.close()












print("--------------------------------------------------------------------------")
#õunad
oun = int(input("Mitu pöialpoissi tahad õunu[0-7]?: "))
õun = 0
for i in range(oun):
    n=random.randint(1, 2)
    print(n)
    õun+=n
summa=14-õun
print(f"Lumivalgukesele jääb {summa} õuna")





#male
nisuterad = 0.5
a = int(input("Sisesta täisarv: "))
i = 0
while i <a:
    i += 1
    nisuterad*=2
print(nisuterad)









#TÄRINGUD
taringud = int(input("Täringute arv?: "))
for i in range(taringud):
    print(random.randint(1, 6))



#Murelikud lapsevanemad
ringid = int(input("Mitu ringi jooksid: "))
ring = 0
porgand = 0
while ring < ringid:
    ring +=1
    if ring %2 == 0:
        porgand+=ring
print(f"porgandite koguarv on {porgand}")
    







"""
#äratus
aratus = int(input("Mitu korda äratus heliseb?: "))
for i in range(aratus):
    print("tõuse ja sära")
"""