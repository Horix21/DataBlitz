import os
import string
import random
import platform
import multiprocessing as mp

i = 0
GB = 1024 ** 3
CSZE = 100
os_name = platform.system()

def program_input(drive):
    print("IAMSLEEPDEPRIVED")
    global GB_input
    GB_input = input("GB: ")
    if GB_input.isdigit():
        GB_input = int(GB_input)
    else:
        print('Invalid input: use "GB: <int>"')
        exit()
    drive.value = input("Location (leave empty for default): ")

def tff():
    c = string.printable
    return "".join(random.choices(c, k=len(c))) * 1000

def changeOS(drive):
    if drive.value == "":
        if os_name == "Windows":
            drive.value = "C:/Users/Public"
        elif os_name == "Linux":
            drive.value = os.path.expanduser('~')
        else:
            print("Default path not found")
            exit()
    return drive.value

def writeFile(i, GB, drive):
    filename = changeOS(drive) + f"/.00{i}"
    with open(filename, "w", buffering=CSZE * 100) as file:
        if(os_name == "Windows"):
            os.system("attrib +h " + filename)
        while True:
            text = tff()
            for _ in range(100):
                file.write(text)
            if os.path.getsize(filename) >= GB:
                file.flush()
                break

def main():
    with mp.Manager() as manager:
        drive = manager.Value('s', "")
        program_input(drive)

        p = []
        for x in range(0, GB_input):
            p.append(mp.Process(target=writeFile, args=(f"{x}000", GB, drive)))
            p[x].start()

        for process in p:
            process.join()

if __name__ == "__main__":
    main()
