# This is a sample Python script.
import os
import random
import hashlib
from functools import cache


Vocabeln = {}

def read_voc():

    for file_name in os.listdir("static/Voc"):
        i = 0
        with open(f"static/Voc/{file_name}") as f:
            file_name = file_name.removesuffix(".txt")
            content = f.readline()
            Vocabeln[file_name] = {}
            while content != "" and content != "\n":
                voc_pair = content.split(":")
                voc_pair[0] = voc_pair[0].rstrip(" ").removesuffix(", v").split(", ")
                voc_pair[1] = voc_pair[1].strip(" \n").removesuffix("(in)").removesuffix("(r)").split(", ")
                i += 1
                content = f.readline()
                Vocabeln[file_name][i] = voc_pair

def randomize(n, letters):

    Rand_Voc = {}
    anzahl = int(n/len(letters))
    for i, letter in enumerate(letters):
        Keys = list(Vocabeln[letter].keys())
        while len(Rand_Voc) < (1+ i) * anzahl:
            temp = random.choice(Keys)
            Rand_Voc[f"{letter}:{temp:04d}"] = Vocabeln[letter][temp]

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

    voc = randomize(n, Letters)
    return format(voc)


read_voc()

if __name__ == '__main__':
    print(get_vocabulary(20,"A","B"))



