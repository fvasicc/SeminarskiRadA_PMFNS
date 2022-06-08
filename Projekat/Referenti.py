# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 23:39:25 2019

@author: Aragog
"""

def login(username, password):
    for r in referenti:
        if r['username'] == username and r['password'] == password:
            return True
    return False
    
def loadRefs():
    for line in open('referenti.txt', 'r').readlines():
        if len(line) > 1:
            ref = str2ref(line)
            referenti.append(ref)

def str2ref(line):
    if line[-1] == '\n':
        line = line[:-1]
    ime, prezime, username, password = line.split('|')
    r = {
      'ime': ime,
      'prezime': prezime,
      'username': username,
      'password': password
    }
    return r

def ref2str(r):
    return '|'.join([r['ime'], r['prezime'], r['username'], r['password']])

referenti = []
loadRefs()