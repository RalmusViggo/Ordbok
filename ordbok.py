telefonbok = [
    
]
telefonbok.append({"navn": "ola", "nummer": 84083049})
telefonbok.append({"navn": "per", "nummer": 78298327})


def vis_alle():
    for person in telefonbok:
        print(person)

vis_alle()