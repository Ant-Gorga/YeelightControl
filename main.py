try:
    import yeelight as yee
except ImportError:
    print("Installa la libreria yeelight per utilizzare questo programma.")
    exit()
import keyboard as kb

def stampaLuci(luci):
    if len(luci) == 0:
        print("Non sono state trovate luci")
        exit()
    print("Sono state trovate le seguenti luci:")
    i=0
    for elem in luci:
        print(i)
        print("Nome:"+ elem["capabilities"]["name"])
        print("Ip:"+ elem["ip"])
        print("Id"+ elem["capabilities"]["id"])
        i+=1
def menu():
    print("Yeelight Control py")
    print("")
    print("1 - Controlla le luci già associate")
    print("")
    print("2 - Associa una nuova luce")
    print("")
    print("3 - Disassocia tutte le luci")
    print("")
    print("4 - Accendi velocemente le luci associate")
    print("")

def associa():
    pass
def main():
    try:
        while True:
            menu()
            while True:
                try:
                    scelta = int(input("Inserisci le il numero corrispondente:"))
                    break
                except ValueError:
                    print("Scelta non valida")
    
            if scelta == 1:
                pass
            elif scelta == 2:
                pass
            elif scelta == 3:
                pass
            elif scelta == 4:
                pass
    except KeyboardInterrupt:
        print("Hai terminato il programma.")
        exit()

print("Ricerca delle luci compatibili in corso . . .")
luci = yee.discover_bulbs()
stampaLuci(luci)
print("Quale luce vuoi controllare?")
while True:
    try:
        tmp = int(input("Inserisci il numero corrispondente: "))
        break
    except ValueError:
        print("Inserisci un valore valido")
luce = yee.Bulb(luci[tmp]["ip"])
lum = luce.get_properties()
lum = int(lum["bright"])
print("Modifica della luminosità.")
print("Premi 'q' per uscire")
while True:
    key = kb.read_key()
    if key == 'q':
        print("Esco. . .")
        break
    if key == "right":
        if(lum == 100):
            print("Luminosità massima")
        else:
            lum+=10
            luce.set_brightness(lum)
    if key == "left":
        if(lum == 0):
            print("Luminosità minima")
        else:
            lum-=10
            luce.set_brightness(lum)

