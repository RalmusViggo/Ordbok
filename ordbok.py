telefonbok = [
    
]
telefonbok.append({"navn": "ola", "nummer": 84083049})
telefonbok.append({"navn": "per", "nummer": 78298327})



def vis_alle():
    for person in telefonbok:
        print(person)

vis_alle()


def leg_til():
    nye = {}
    nye["navn"] = input("skriv inn ditt navn: ")
    nye["nummer"] = int(input("skriv inn ditt nummer: "))
    print(f"{nye} ble lagt til i telefonboken")
    return telefonbok.append(nye)
    
    #nye({"navn": input("skriv inn ditt navn: "), "nummer": int(input("skriv inn ditt nummer: "))})

leg_til()
print(telefonbok)


def sok():
    navn = input("skriv inn navnet du vil søke etter: ")
    for n in telefonbok:
        if n["navn"] == navn:
            print(n)
            break
        else:
            print("dette navnet finnes ikke")
            break

sok()