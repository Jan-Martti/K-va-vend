#J.M.O
#14.11.22
#iseseisev töö

#kuupäev
def loll(s):
    kuud = [" ","jaan","veeb","marts","april","mai","juuni","juuli","august","september","oktober","november","detsember"]
    return kuud[s]

def segs (f):
    




#mündid
ho=[]
fail = input("Sisestage failinimi: ")
debil = open(fail)
for i in debil:
    ho.append(int(i.strip("\n")))
def pronksikarva_summa(p):
    for i in p:
        p[:]=[x for x in p if x<=5]
    print(f"Hoiupõrsasse läheb {sum(p)} senti")
pronksikarva_summa(ho)
    
    
    
    
    
    
    


    
    














#tervitused mõtisklustega
def tervitus(k):
    print('Võõrustaja: "Tere!"')
    print(f"Täna {k}. kord tervitada, mõtiskleb võõrustaja")
    print('Külaline: "Tere, suur tänu kutse eest!"')
    
    

kulalised = int(input("Mitu külalist tuleb: "))
for i in range(kulalised):
    tervitus(i+1)










#peo eelarve


def eelarve(e):
    l = e*10+55
    return l

k = int(input("Mitu kutsutud: "))
print(eelarve(k))
t = int(input("Mitu tuleb: "))
print(eelarve(t))


#Õunamahla tegemine

o = int(input("Õunte kogus (kg): "))

def mahlapakkide_arv(o):
    k = o*0.4/3
    return k


print(mahlapakkide_arv(o))



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