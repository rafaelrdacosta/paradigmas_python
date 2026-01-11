# Função recursiva de contagem regressiva

import time

def regressiva(x):
    print(x)
    time.sleep(1)
    if x > 0:
        regressiva(x - 1)
    else:
        print('Acabou!')

regressiva(10)

# Função não recursiva
for y in range(10, -1, -1):
    print(y)
    time.sleep(1)
print('Acabou!')