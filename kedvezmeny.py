# 1. lépés: bekérjük a vendégek számát
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
