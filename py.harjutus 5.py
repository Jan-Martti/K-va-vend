#J.M.O
#25.10.2022
#harjutus 05

#vanused tärnidega
vanused = [13,67,69,43,46,86,78,34,21,49]
for i in vanused:
    vanused+=1
        



#vanused
vanused = [13,67,69,43,46,86,78,34,21,49]

print(f"Vanim {max(vanused)}")
print(f"Noorim {min(vanused)}")
print(f"Vanuste summa {sum(vanused)}")
print(f"Keskmine vanus {sum(vanused)/len(vanused)}")

#Duplikaadid




opilased = ["Juhan","Kati","Mario","Mario","Mati","Mati"]
puh_opilased = []
for i in opilased:
    if i not in puh_opilased:
        puh_opilased.append(i)


print(puh_opilased)


"""
print("---------------------------")
#Õpilased
jrk = 1
opilased = ["Juhan","Kati","Maarja","Mario","Mati"]
for i in opilased:
    print(f"{jrk}. {i}")
    jrk+=1
#Küsi millist tahab muuta
nr = int(input("Mitmendat nime tahad muuta: "))
nr-=1
#ja milleks muudab
opilane = input("Milleks muudate: ")
#tee muudatus
del opilased[nr]
opilased.insert(nr, opilane)

print(opilased)

print("---------------------------")
#Nimede lisamine loendisse

nimed = []
for i in range(5):
    nimi = input("Lisa nimi loendisse: ")
    nimed.append(nimi)
nimed.sort()
print(nimed)
print(f"Viimati lisatud nimi: {nimed[-1]}")
"""
