#J.M.O
#21.11.2022
#3. Täringud
#kuvatakse korrektne arusaadav küsimus ja hiljem vastus
#kasutaja võistleb kahe täringuga arvuti vastu
#kasutaja teeb pakkumise ning suurima täringupunktisumma võitja saab laual oleva raha endale (if win then get all money)
#kogu looming salvestatakse tekstifaili
#kood kommenteeritud
import random




#Suvaliste arvude genereerimine
def dice():
    t = int(input("Mis summaga lauda tuled: "))
    r = int(input("Mis summa paned mängu: "))
    dice = random.randint(1, 12)
    dice2 = random.randint(1, 12)
    
    if dice > dice2:
        s = t +r
        print(s)
        print("Mina võitsin")
    elif dice < dice2:
        s = t - r
        print(s)
        print("Mina kaotasin")
    else:
        print("Mäng on viigis")
        print("Raha tagasi")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

dice() 
        
        
        
    
    
    
        
        
        
        