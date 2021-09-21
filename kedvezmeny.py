# 1. lépés: bekérjük a vendégek számát PIPA
# 2. lépés: megnézzük ez pontosan hány százalék az első kedvezményben
# 3. lépés: megnézzük ez pontosan hány százalék a második kedvezményben
# 4. lépés: megnézzük ez pontosan hány százalék a harmadik kedvezményben
# 5. lépés: összevetjük a kedvezményeket
# 6. lépés: megmondjuk a felhasználónak, hogy melyik a legnagyobb kedvezmény

def bekeres():
    diakok = None
    while diakok == None:
        try:
            user_input = int(input("Diákok száma: "))
        except ValueError:
            print("Egész számot adj meg!")
            continue
        
        if user_input >= 1 and user_input <= 100:
            diakok = user_input
        else:
            print("1-nél nem kisebb és 100-nál nem nagyobb számot adj meg!")

    return diakok


def csoportos_kedvezmeny(diakok_szama):
    cskedvezmeny = None
    if diakok_szama < 10:
        cskedvezmeny = 0
    elif diakok_szama < 20:
        cskedvezmeny = 0.05
    elif diakok_szama < 30:
        cskedvezmeny = 0.08
    elif diakok_szama < 41:
        cskedvezmeny = 0.12
    else:
        cskedvezmeny = 0.14

    return cskedvezmeny
        
    

diakok_szama = bekeres()

