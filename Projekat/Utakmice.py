# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 22:49:54 2019

@author: Aragog
"""

def loadGames():
    for line in open('utakmice.txt', 'r').readlines():
        if len(line) > 1:
            u = str2game(line)
            utakmice.append(u)

def saveGame():
    file = open('utakmice.txt', 'w')
    for u in utakmice:
        file.write(game2str(u))
        file.write('\n')
    file.close()
    
def addGames(utakmica):
    utakmice.append(utakmica)
    
def str2game(line):
    if line[-1] == '\n':
        line = line[:-1]
    datum, protivnik, ishod = line.split('|')
    game = {
      'datum': datum,
      'protivnik': protivnik,
      'ishod': ishod
    }
    return game

def game2str(i):
    return '|'.join([i['datum'], i['protivnik'], i['ishod']])

def formatHeader():
    return \
      "Datum       |Protivnik    \n" \
      "------------+--------------------"

def formatPlayer(u):
    return u"{0:12}|{1:20}".format(
      u['datum'],
      u['protivnik'])

    
utakmice = []
loadGames() 