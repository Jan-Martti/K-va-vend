#J.M.O
#27.10.2022
#harjutus06


minu_fail = open("s6pru_l6ustaraamatus.txt", "r")

reformikad = 0
kesikud = 0
erakonnad = []

for i in minu_fail.readlines():
    enimi,pnimi,er,palk = i.split(" ")
    if er=="RE":
        reformikad+=1
    elif er=="KE":
        kesikud+=1
    if er not in erakonnad:
        erakonnad.append(er)
    with open("loll.txt","a") as fail_loll:
        fail_loll.write(enimi + " " +pnimi +"\n")
        
        
print(f"Reformikaid kokku: {reformikad}")
print(f"Kesikud kokku: {kesikud}")
print(f"Erakondi kokku: {len(erakonnad)}")




minu_fail.close
