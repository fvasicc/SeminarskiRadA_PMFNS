# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 23:44:46 2019

@author: Aragog
"""

def loadPlayers():
    for line in open('igraci.txt', 'r').readlines():
        if len(line) > 1:
            u = str2player(line)
            igraci.append(u)
            
def savePlayer():
    file = open('igraci.txt', 'w')
    for i in igraci:
        file.write(player2str(i))
        file.write('\n')
    file.close()
        
def addPlayer(igrac):
    igraci.append(igrac)
    
def str2player(line):
    if line[-1] == '\n':
        line = line[:-1]
    ime, prezime, datum, visina, tezina = line.split('|')
    igraci = {
      'ime': ime,
      'prezime': prezime,
      'datum': datum,
      'visina': visina,
      'tezina': tezina
    }
    return igraci

def player2str(i):
    return '|'.join([i['ime'], i['prezime'], 
      i['datum'], i['visina'], i['tezina']])

def formatHeader():
    return \
      "Ime       |Prezime     |Datum rodj. |Visina |Tezina\n" \
      "----------+------------+------------+-------+-------"

def formatPlayer(u):
    return u"{0:10}|{1:12}|{2:12}|{3:>7}|{4:>7}".format(
      u['ime'],
      u['prezime'],
      u['datum'],
      u['visina'],
      u['tezina'])

def formatPlayers(playerList):
    result = ""
    for player in playerList:
        result += formatPlayer(player) + '\n'
    return result

def formatAllPlayers():
    result = ''
    for i in igraci:
        result += "{0:10}|{1:12}|{2:10}|{3:>5}|{4:>5}".format(
      i['ime'],
      i['prezime'],
      i['datum'],
      i['visina'],
      i['tezina'],) + '\n'
    return result
        
def sortPlayer(key):
    igraci.sort(key = lambda x: x[key])
    
print(__name__)  
igraci = []
loadPlayers() 