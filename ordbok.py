import time
telefonbok = [
    
]
telefonbok.append({"navn": "ola", "nummer": 84083049})
telefonbok.append({"navn": "per", "nummer": 78298327})


       

def vis_alle():
    for person in telefonbok:
        print(person)




def legg_til():
    nye = {}
    nye["navn"] = input("skriv inn ditt navn: ")
    nye["nummer"] = int(input("skriv inn ditt nummer: "))
    print(f"{nye} ble lagt til i telefonboken")
    return telefonbok.append(nye)
    
    #nye({"navn": input("skriv inn ditt navn: "), "nummer": int(input("skriv inn ditt nummer: "))})




def sok():
    navn = input("skriv inn navnet du vil søke etter: ")
    for n in telefonbok:
        if n["navn"] == navn.lower():
            print(n)
            break



def w():
    while True:
        en = 1
        print(f"1. Vis alle.")
        to = 2
        print("2. Legg til ny")
        tre = 3
        print("3. Søk")
        fire = 4
        print("4. Avslutt ")
        valg = int(input("skriv tallet foran det du vil gjøre: "))
        if valg == 1:
            vis_alle()
            time.sleep(0.5)
        elif valg == 2:
            legg_til()
            time.sleep(0.5)
        elif valg == 3:
            sok()
            time.sleep(0.5)
        elif valg == 4:
            print("programmet avsluttes")
            break

w()