# your code goes here!

import time

def Run_count():
    x = 1
    while x < 10:
        print(f"{x} is less than 10.")
        x += 1

print(Run_count())


def countdown():
    y = 10
    while y > 0:
        print(f"{y} SECOND(S)!")
        y -= 1
    print(f"HAPPY NEW YEAR!")
    
print(countdown())

def countdown_with_sleep():
    z = 10
    while z > 0:
        print(f"waiting for 1sec before {z} run!")
        z -= 1
        time.sleep(1)
    print(f"HAPPY NEW YEAR!")
print(countdown_with_sleep())