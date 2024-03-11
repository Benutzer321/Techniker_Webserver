import os
import random
import time

Bingo = {}
def load_Bingo_from_files():
    for file_name in os.listdir("static/Bingo"):
        Bingo.update({file_name.removesuffix(".txt"): []})
        with open(f"static/Bingo/{file_name}", "r", encoding="utf-8") as f:
            for line in f.readlines():
                Bingo[file_name.removesuffix(".txt")].append(line)
    return True


def create_random_Bingo_token(name, size):

    if len(Bingo[name]) < size:
        return None

    samples = random.sample(range(0,len(Bingo[name])),size)

    token = "#".join(str(x) for x in samples)

    return token


def load_Bingo(Name,code):
    samples = code.split("#")
    values = [Bingo[Name][int(x)] for x in samples]
    return values


load_Bingo_from_files()
__loaded_at__ = time.time()

if __name__ == "__main__":
    token = create_random_Bingo_token("Stark",3**2)
    print(load_Bingo("Stark",token))