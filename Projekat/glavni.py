# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 23:39:10 2019

@author: Aragog
"""

import Referenti
import Igraci
import Statistika
import Utakmice
import matplotlib.pyplot as plt

def main():
    print()
    print( "Pocetna strana kk-a")
    print( "====================")
    print()
    if not login():
        print( "\nNiste uneli postojece ime i lozinku!")
        return
    komanda = '0'
    while komanda != 'X':
        komanda = menu()
        if komanda == '1':
            addPlayer()
        elif komanda == '2':
            addStats()       
        elif komanda == '3':
            addGame()
        elif komanda == '4':
            printAllPlayers()
        elif komanda == '5':
            averageStats()
        elif komanda == '6':
            playersStats()
        elif komanda == '7':
            printGames()
        elif komanda == '8':
            winlose()
        elif komanda == '9':
            playerIndexRating()
    print( "Dovidjenja.")

def menu():
    printMenu()
    command = input(">> ")
    while command.upper() not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', 'X'):
        print( "\nUneli ste pogresnu komandu.\n")
        printMenu()
        command = input(">> ")
    return command.upper()

def printMenu():
    print( "\nIzaberite opciju:")
    print( "  1 - Unosenje novog igraca")
    print( "  2 - Upisivanje statistike igraca sa utakmice")
    print( "  3 - Dodavanje nove utakmice")
    print( "  4 - Pregledati igrace u klubu")
    print( "  5 - Prosecna statistika igraca")
    print( "  6 - Statistika igraca sa utakmice(Uneti datum utakmice)")
    print( "  7 - Prikaz odigranih utakmica")
    print( "  8 - Grafikon pobede-porazi")
    print( "  9 - Grafikon igrac-indeks korisnosti")
    print( "  x - izlaz iz programa")

def login():
    username = input("Korisnicko ime >> ")
    password = input("Lozinka >> ")
    return Referenti.login(username, password)

def addPlayer():
    print("Unos novog igraca\n")
    i = {}
    i['ime'] = input("Unesite ime >> ")
    i['prezime'] = input("Unesite prezime >> ")
    i['datum'] = input("Unesite datum rodjenja >> ")
    i['visina'] = input("Unesite visinu igraca u centimetrima >> ")
    i['tezina'] = input("Unesite tezinu igraca u kilogramima >> ")
    Igraci.addPlayer(i)
    Igraci.savePlayer()

def addStats():
    print("Unos statistike igraca sa utakmice \n")
    s = {}
    s['datum'] = input("Unesite datum utakmice(DD.MM.YYYY.) >> ")
    s['igrac'] = input("Unesite ime i prezime igraca>> ")
    s['poeni'] = input("Unesite broj poena igraca >> ")
    s['asistencije'] = input("Unesite broj asistencija igraca >> ")
    s['skokovi'] = input("Unesite broj skokova igraca >> ")
    s['blokade'] = input("Unesite broj blokada igraca >> ")
    s['ukrlopte'] = input("Unesite broj ukradenih lopti igraca >> ")
    s['faulovi'] = input("Unesite broj faulova igraca >> ")
    Statistika.addStats(s)
    Statistika.saveStats()

def addGame():
    print("Dodavanje nove odigrane utakmice \n")
    g = {}
    g['datum'] = input("Unesite datum utakmice(DD.MM.YYYY.) >> ")
    g['protivnik'] = input("Unesite protivnika >> ")
    g['ishod'] = input("Unesite ishod utakmice(w za pobedu, l za poraz >> ")
    Utakmice.addGames(g)
    Utakmice.saveGame()

def printAllPlayers():
    print("Svi igraci u klubu \n")
    print(Igraci.formatHeader())
    for igrac in Igraci.igraci:
        print(Igraci.formatPlayer(igrac))

def averageStats():
    print("Prosecna statistika igraca tokom sezone \n")
    print(Statistika.formatHeader())
    allplayers = set([i['igrac'] for i in Statistika.statistika])
    for igrac in allplayers:
        playerstats = Statistika.findPlayer(igrac)
        poeni = [int(i['poeni']) for i in playerstats]
        prosek_poena = sum(poeni)/len(poeni)
        asist = [int(i['asistencije']) for i in playerstats]
        prosek_as = sum(asist)/len(asist)
        skok = [int(i['skokovi']) for i in playerstats]
        prosek_skok = sum(skok)/len(skok)
        blok = [int(i['blokade']) for i in playerstats]
        prosek_blok = sum(blok)/len(blok)
        ul = [int(i['ukrlopte']) for i in playerstats]
        prosek_ul = sum(ul)/len(ul)
        faul = [int(i['faulovi']) for i in playerstats]
        prosek_faul = sum(faul)/len(faul)
        print("{0:25}|{1:>6.2f}|{2:>6.2f}|{3:>6.2f}|{4:>6.2f}|{5:>6.2f}|{6:>6.2f}".format(igrac,prosek_poena,prosek_as,
              prosek_skok,prosek_blok,prosek_ul,prosek_faul))

def playersStats():
    utakmica = input("Unesite datum utakmice(DD.MM.YYYY.) >> ")
    print(' ')
    print("Statistika igraca sa utakmice odigrane",utakmica,"\n")
    if not Statistika.gamedata(utakmica):
        print("Za uneti datum ne postoji odigrana utakmica.")
    else:
        print(Statistika.formatHeader())
        for i in Statistika.statistika:
            if utakmica in i['datum']:
                print(Statistika.formatPlayer(i))

def printGames():
    print("Sve odigrane utakmice \n")
    print(Utakmice.formatHeader())
    for utakmica in Utakmice.utakmice:
        print(Utakmice.formatPlayer(utakmica))

def winlose():
    allgames = [i['ishod'] for i in Utakmice.utakmice]
    pobede=0
    porazi=0
    for i in allgames:
        if i == 'w':
            pobede+=1
        else:
            porazi+=1
    
    width = 0.1
    fig, ax = plt.subplots()
    rects1 = ax.bar(1 - width/2, pobede, width, label = 'Pobede')
    rects2 = ax.bar(1 + width/2, porazi, width, label = 'Porazi')
    ax.set_ylabel('Broj pobeda i poraza')
    ax.set_title('Broj pobeda i poraza u sezoni')
    ax.legend()
    plt.show()

def playerIndexRating():
    x_podaci = []
    y_podaci = []
    
    print("Prosecan indeks korisnosti \n" )
    allplayers = set([i['igrac'] for i in Statistika.statistika])
    for igrac in allplayers:
        playerstats = Statistika.findPlayer(igrac)
        poeni = [int(i['poeni']) for i in playerstats]
        asist = [int(i['asistencije']) for i in playerstats]
        skok = [int(i['skokovi']) for i in playerstats]
        blok = [int(i['blokade']) for i in playerstats]
        ul = [int(i['ukrlopte']) for i in playerstats]
        faul = [int(i['faulovi']) for i in playerstats]
        brojutakmica = [i['datum'] for i in playerstats]
        index = (sum(poeni)+sum(asist)+sum(skok)+sum(blok)+sum(ul)-sum(faul))/len(brojutakmica)
        print("{0} {1:.2f}".format(igrac,index))
        
        x_podaci.append(igrac)
        y_podaci.append(index)

    plt.bar(x_podaci, y_podaci)
    plt.xlabel('igraci')
    plt.xticks(rotation=90)
    plt.ylabel('index')
    plt.ylim(ymin=0, ymax=50)
    plt.show()
        

print(__name__)    
if __name__ == '__main__':
    main()