import time
s=input("Enter time in number of seconds")
def countdown(s):
    m = int(s/60)
    sec = int(s%60)
    t = f'{m}:{sec}'
    print(t)
countdown(int(s))