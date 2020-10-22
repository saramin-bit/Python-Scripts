import random
import time

coin = ['Heads', 'Tails']

def coinflip():
    rnd = round(random.uniform(0, 1))
    flip = coin[rnd]
    print('You flipped the coin...')
    time.sleep(1)
    print(flip + '!!')

coinflip()
