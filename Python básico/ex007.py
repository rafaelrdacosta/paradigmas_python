#Blocos - são definidos por identação
#São iniciados por dois pontos (:) e nas linhas inferiores incia-se com um TAB (4 espaços)

a = 0
for i in range(30):
    if a % 2 == 0:
        a += 1
        continue
    else:
        if a % 5 == 0:
            break
        else:
            a += 3
print(a)