import time
import os

t = [0, "day(s)", 0, "hour(s)", 0, "minute(s)", 0,"second(s)"]

def timer():
    print(f"{t[0]} {t[1]} {t[3]} {t[4]} {t[5]} {t[6]} {t[7]}")
    time.sleep(1)
    if t[-2] == 59:
        t[-2] = 0
        t[-4] = t[-4] + 1
    if t[-4] == 59:
        t[-4] = 0
        t[2] = t[2] + 1
    else:
        t[-2] = t[-2] + 1
    os.system("clear")

while True:
    timer()