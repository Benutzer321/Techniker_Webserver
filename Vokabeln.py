# This is a sample Python script.
import os
import random
import hashlib
from functools import cache

import re
pattern = r"\(.*?\)|\n"

Vocabeln = {}

def read_voc():

    for file_name in os.listdir("static/Voc"):
        i = 0
        with open(f"static/Voc/{file_name}", "r", encoding="utf-8") as f:
            file_name = file_name.removesuffix(".txt")
            content = f.readline()
            Vocabeln[file_name] = {}
            while content != "" and content != "\n":
                voc_pair = content.split(":")
                voc_pair[0] = re.sub(pattern, "", voc_pair[0].rstrip(" ").removesuffix(", v")).split(", ")
                voc_pair[1] = re.sub(pattern, "", voc_pair[1]).split(", ")
                i += 1
                content = f.readline()
                Vocabeln[file_name][i] = voc_pair

def randomize(n, letters):

    Rand_Voc = {}

    while len(Rand_Voc) < n:
        key = random.choice(letters)
        element = random.randint(1, len(Vocabeln[key]))
        Rand_Voc[f"{key}:{element:04d}"] = Vocabeln[key][element].copy()

    for i in Rand_Voc.values():
        if random.randint(0,1):
            i.reverse()

    return Rand_Voc

def vocabel_hilfe(vocabel):
    voc = []
    rand = random.randint(1,int(len(vocabel) * 0.2) + 1)
    for i in range(0, len(vocabel)):
        if i <= rand:
            voc.append(vocabel[i])
            continue
        if vocabel[i] in [" ", "(", ")"]:
            voc.append(vocabel[i])
            continue

        voc.append("?")
    return "".join(voc)

def hash_loesung(voc):
    voc_return = []
    for i in voc:
        voc_return.append(hashlib.sha1(i.encode()).hexdigest())
    return voc_return


def format(voc):
    for v in voc.values():
        v[0] = random.choice(v[0])
        v.append(vocabel_hilfe(random.choice(v[1])))
        v[1] = hash_loesung(v[1])
    return voc

def get_vocabulary(n,Letters):

    for letter in Letters:
        if letter not in Vocabeln.keys():
            return None
    if n > sum([len(Vocabeln[letter]) for letter in Letters]):
        return None

    return format(randomize(n, Letters))

def check_parameters(n, Letters):
    for letter in Letters:
        if letter not in Vocabeln.keys():
            return "Vokabeln nicht gefunden"
    if n > sum([len(Vocabeln[letter]) for letter in Letters]):
        return "Zu viele Vokabeln"
    


read_voc()

if __name__ == '__main__':
    print(get_vocabulary(20,"A","B"))



