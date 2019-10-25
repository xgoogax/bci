import time 
import pandas as pd
import numpy as np

print(time.time())
start_time = time.time()
duration = 5 #ms 
n_repetitions = 30
bodzce_lewa_start = []

for i in range(n_repetitions):
    print('relaks')
    time.sleep(duration)
    bodzce_lewa_start.append(time.time())
    print('lewa reka')
    time.sleep(duration)

bodzce_prawa_start = []

for i in range(n_repetitions):
    print('relaks')
    time.sleep(duration)
    bodzce_prawa_start.append(time.time())
    print('prawa reka')
    time.sleep(duration)


df = pd.DataFrame(np.array([bodzce_lewa_start, bodzce_prawa_start]).T, columns=['lewa', 'prawa'])
df.to_csv('start_time.csv')