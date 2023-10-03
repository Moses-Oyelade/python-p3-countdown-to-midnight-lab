# your code goes here!

import time

# def Run_count():
#     x = 1
#     while x < 10:
#         print(f"{x} is less than 10.")
#         x += 1

# print(Run_count())


def countdown(y):
    
    while y > 0:
        print(f"{y} SECOND(S)!")
        y -= 1
    print(f"HAPPY NEW YEAR!")
    
print(countdown(10))

def countdown_with_sleep(z):
    while z >= 1:
        print(f"{z} SECONDS(S)!")
        z -= 1
        time.sleep(1)
        
        
    print("HAPPY NEW YEAR!")
print(countdown_with_sleep(10))