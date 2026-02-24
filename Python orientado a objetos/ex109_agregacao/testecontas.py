#Realizando a agregação
from conta import Conta
from cliente import Cliente

cliente1 = Cliente(64194159349, 'Rafael', 'Rua Mal Mallet, 3')
cliente2 = Cliente(12345678989, 'José Leôncio', 'Rua Hermes da Fonseca, 12')

conta1 = Conta([cliente1, cliente2], 1, 0)


conta1.gerarsaldo()
conta1.depositar(1500)
conta1.gerarsaldo()
conta1.sacar(500)
conta1.gerarsaldo()