from Classes.Contadec import Contadec

def main():
    conta = Contadec(1)
    conta.saldo = 1000
    print(f'Saldo da Conta = {conta.saldo}')

if __name__ == '__main__':
    main()