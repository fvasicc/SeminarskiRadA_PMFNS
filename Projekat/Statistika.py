# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 22:23:41 2019

@author: Aragog
"""

def loadStats():
    for line in open('statistika.txt', 'r').readlines():
        if len(line) > 1:
            s = str2stat(line)
            statistika.append(s)

def saveStats():
    file = open('statistika.txt', 'w')
    for s in statistika:
        file.write(stats2str(s))
        file.write('\n')
    file.close()
    
def addStats(i):
    statistika.append(i)
             
def str2stat(line):
    if line[-1] == '\n':
        line = line[:-1]
    datum, igrac, poeni, asistencije, skokovi, blokade, ukrlopte, faulovi = line.split('|')
    stats = {
      'datum': datum,
      'igrac': igrac,
      'poeni': poeni,
      'asistencije': asistencije,
      'skokovi': skokovi,
      'blokade': blokade,
      'ukrlopte': ukrlopte,
      'faulovi': faulovi
    }
    return stats

def stats2str(s):
    return '|'.join([s['datum'], s['igrac'], s['poeni'], s['asistencije'],s['skokovi'], s['blokade'],
                    s['ukrlopte'], s['faulovi']])

def allStats():
    return statistika

def formatHeader():
    return \
      "Ime i prezime            |Poeni |Asist.|Skok. |Blok. |U.lop.|Faul. \n" \
      "-------------------------+------+------+------+------+------+------"

def formatPlayer(u):
    return u"{0:25}|{1:>6}|{2:>6}|{3:>6}|{4:>6}|{5:>6}|{6:>6}".format(
      u['igrac'],
      u['poeni'],
      u['asistencije'],
      u['skokovi'],
      u['blokade'],     
      u['ukrlopte'],      
      u['faulovi'])

def formatPlayers(playerList):
    result = ""
    for player in playerList:
        result += formatPlayer(player) + '\n'
    return result

def findPlayer(igrac):
    result = []
    for s in statistika:
        if s['igrac'].upper() == igrac.upper():
            result.append(s)
    return result

def gamedata(datum):
    for s in statistika:
        if s['datum'] == datum:
            return True
    return False

statistika = []
loadStats() 