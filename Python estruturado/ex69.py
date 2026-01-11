# Função fatorial recursiva
def fatorial_rec(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial_rec(n-1)

vfat = fatorial_rec(5)
print(f'Resultado fatorial recursivo: {vfat}')

# Função fatorial não recursivo
def fatorial(n):
    fat = 1
    if n == 0 or n == 1:
        return 1
    else:
        for x in range(2, n + 1):
            fat = fat * x
        return fat
vfat_rec = fatorial(5)
print(f'Resultado fatorial: {vfat_rec}')

