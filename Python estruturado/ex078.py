# Módulo time

import time
#time retorna o total de de segundos desde a "Epoch" - marco zero do tempo no Unix
# 1º de janeiro de 1970
print(time.time())

'''laocaltime retorna um objeto estruturado chamado struct_time
time.struct_time(tm_year=2026, tm_mon=2, tm_mday=15, tm_hour=19, 
tm_min=53, tm_sec=3, tm_wday=6, tm_yday=46, tm_isdst=0)'''
print(time.localtime())

x = time.time()
#ctime retorna uma string com o seguinte formato: Sun Feb 15 19:55:00 2026
print(f'Local time: {time.ctime(x)}')