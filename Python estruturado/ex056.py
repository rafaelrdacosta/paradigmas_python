for num in range(1000, 10000):
    # obtem o nr dos algarismos menos significativos
    menor = num % 100
    # obtem o nr dos algarismos mais significativos
    maior = num // 100
    raiz = menor + maior

    if (raiz * raiz) == num:
        print(num)
        print(menor)
        print(maior)
        print(raiz)
print('terminou')
print('saiu ', num)
