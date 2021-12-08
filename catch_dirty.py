import json
import re
import csv
import pandas as pd


with open('new_all_17.json', 'r', encoding = 'utf-8') as f:
    followers = json.load(f)

num = 0;
datalist=[]
t=0

for f in followers:
    t+=1
    # physical aggression

    '''fuck = bool(re.search(r'\b(F|f)uck\b', f['content'])) #1509
    bitch = bool(re.search(r'\b(B|b)itch\b', f['content'])) #493
    shot = bool(re.search(r'\b(S|s)hot\b', f['content'])) #1434
    kill = bool(re.search(r'\b(K|k)ill\b', f['content'])) #1096
    murder = bool(re.search(r'\b(M|m)urder\b', f['content'])) #875
    stab = bool(re.search(r'\b(S|s)tab\b', f['content'])) #19
    shit = bool(re.search(r'\b(S|s)hit\b', f['content'])) #3004
    cunt = bool(re.search(r'\b(C|c)unt\b', f['content'])) #16
    motherfucker = bool(re.search(r'\b(M|m)otherfucker\b', f['content'])) #27
    pussy = bool(re.search(r'\b(P|p)ussy\b', f['content'])) #194
    bastard = bool(re.search(r'\b(B|b)astard\b', f['content'])) #87
    cock = bool(re.search(r'\b(C|c)ock\b', f['content']))  # 27
    dick = bool(re.search(r'\b(D|d)ock\b', f['content']))  # 28
    ass = bool(re.search(r'\b(A|a)ss\b', f['content']))  # 1900
    asshole = bool(re.search(r'\b(A|a)sshole\b', f['content'])) #416
    die = bool(re.search(r'\b(D|d)ie\b', f['content']))  # 1469
    dead = bool(re.search(r'\b(D|d)ead\b', f['content']))  # 1595
    nigga = bool(re.search(r'\b(N|n)igga\b', f['content']))  # 75
    nigger = bool(re.search(r'\b(N|n)igger\b', f['content']))  # 8
    twat = bool(re.search(r'\b(T|t)wat\b', f['content']))  # 14
    faggot = bool(re.search(r'\b(F|f)aggot\b', f['content']))  # 4
    retarded = bool(re.search(r'\b(R|r)etarded\b', f['content']))  # 32
    redneck = bool(re.search(r'\b(R|r)edneck\b', f['content']))  # 20'''
    trash = bool(re.search(r'\b(T|t)rash\b', f['content']))  # 666

    if trash:
        num += 1
        data = dict(account = f['account'],id = f['id'],content = f['content'], count = num )
        datalist.append(data)

print(t)

with open('physical_trash.json', 'w', encoding='utf-8') as f:
    json.dump(datalist, f, ensure_ascii=False, indent=4)
