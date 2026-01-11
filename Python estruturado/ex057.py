for raiz in range(32, 100):
    num = raiz * raiz
    menor = num % 100
    maior = num // 100

    if (menor + maior) == raiz:
        print(num)
        print(menor)
        print(maior)
        print(raiz)
print('terminou')
print('saiu ', raiz)