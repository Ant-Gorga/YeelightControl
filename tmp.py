try:
    import yeelight as yee
except ImportError:
    print("Installa la libreria yeelight per utilizzare questo programma.")
    exit()
import keyboard as kb

class saved_light:
    """Classe semplificata per lo store delle luci"""
    

saved_lights = []
filename= "data.txt"

def int_input(inizio : int,fine:int):
    while True:
        try:
            scelta = int(input("Inserisci le il numero corrispondente:"))
            if scelta< inizio or scelta > fine:
                print("La scelta corrispondente non esiste.")
                continue
            break
        except ValueError:
            print("Scelta non valida")
    return scelta

def get_saved_lights():
    try:
        with open(filename,"r") as read:
            lines = read.readlines()
            if len(lines) == 0:
                print("il file è vuoto")
                return
            for l in lines:
                tmp = l.split(",") ##name,ip,id
                saved_lights.append({"name":tmp[0],"ip":tmp[1],"id":tmp[2].rstrip("\n")})#tolgo il newline

    except FileNotFoundError:
        print("File non trovato, lo creo.")
        with open(filename,"w") as f:
            f.close()
    
def print_lights(lights):
    print("Sono state trovate le seguenti luci:")
    i=0
    for elem in lights:
        print(i)
        print("Nome:"+ elem["capabilities"]["name"])
        print("Ip:"+ elem["ip"])
        print("Id"+ elem["capabilities"]["id"])
        i+=1

def add_light(light: yee.Bulb,from_saved: bool):
    if from_saved:
        for sav_light in saved_lights:
            if sav_light["id"]==light["capabilities"]["id"]:
                print("La luce è già associata")
                return
        with open(filename,"a") as f:
            f.write("{},{},{}".format(light["capabilities"]["name"],light["ip"],light["capabilities"]["id"]))
            f.write("\n")
            print("Luce salvata")
    else:
        for sav_light in saved_lights:
            if sav_light["id"]==light["capabilities"]["id"]:
                print("La luce è già associata")
                return
        with open(filename,"a") as f:
            f.write("{},{},{}".format(light["capabilities"]["name"],light["ip"],light["capabilities"]["id"]))
            f.write("\n")
            print("Luce salvata")

def menu():
    print("YeelightControl.py")
    print("0 - Termina")
    print("")
    print("1 - Controlla le luci già associate.")
    print("")
    print("2 - Associa una nuova luce.")
    print("")
    print("3 - Disassocia tutte le luci.")
    print("")
    print("4 - Toggle delle luci associate.")
    print("")

def del_file():
    with open(filename,"w") as f:
        f.write("") 

def check_ip_change():
    lights = yee.discover_bulbs()
    changes = False
    for i in range(0,len(lights)):
        for j in range(0,len(saved_lights)):
            if lights[i]["capabilities"]["id"]==saved_lights[j]["id"]:
                if lights[i]["ip"]!=saved_lights[j]["ip"]:
                    saved_lights[j]["ip"]=lights[i]["ip"]
                    print("Just for debug")
                    changes = True
    if changes:
        del_file()
        for l in saved_lights:
            add_light(l,True)
def main():
    get_saved_lights()
    check_ip_change()
    try:
        while True:
            menu()
            scelta = int_input(0,4)
            if scelta == 1:
                print("Scegli quale luce vuoi controllare:")
                get_saved_lights()
                sc = int_input(0,((len(saved_lights)-1)/2))
                print("Ciao")
                ####Controllare la luce

            elif scelta == 2:
                luci = yee.discover_bulbs()
                if len(luci)==0:
                    print("Non ho trovato luci nella tua rete")
                else:
                    print_lights(luci)
                    sc = int_input(0,len(luci)-1)
                    add_light(luci[sc])
                get_saved_lights()

            elif scelta == 3:
                del_file()
                print("Luci associate eliminate")
                get_saved_lights()

            elif scelta == 4:
                for light in saved_lights:
                    luce = yee.Bulb(light["ip"])
                    luce.toggle()
                    print("Toggle di {}".format(light["name"]))
            elif scelta == 0:
                raise KeyboardInterrupt
            else:
                print("La scelta corrispondente non esiste")
    except KeyboardInterrupt:
        print("\n\nHai terminato il programma.")
        exit()

main()