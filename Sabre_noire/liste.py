Liste=[50000,120000,30000,150000]
compteur=0
summe=0
for i in Liste:
    summe+=i
    compteur+=1
    for prix in range(i):
        if prix>40000:
            moyenne=summe/compteur
            print(f"la moyenne est de:,{moyenne}")