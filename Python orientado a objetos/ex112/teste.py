from class_livro import livro
from class_biblioteca import biblioteca

#Testando as classes
#Criando alguns livros

livro1 = livro('O Senhor dos Anéis', 'J.R.R. Tolkien', '123456')
livro2 = livro('1984', 'George Orwel', '343567')
livro3 = livro('O Apanhador no Campo de Centeiro', 'J.D. Salinger', '783575')

#Criando uma biblioteca
biblioteca = biblioteca('Biblioteca Central')

#Adicionando livros a biblioteca
biblioteca.adicionar_livros(livro1)
biblioteca.adicionar_livros(livro2)
biblioteca.adicionar_livros(livro3)

#Listando todos os livros na biblioteca
biblioteca.listar_livros()

#Removendo um livro da biblioteca
biblioteca.remover_livros('783575')

#Listando os livros na biblioteca após a remoção
biblioteca.listar_livros()

#Buscando um livro pelo título
biblioteca.buscar_livro('1984')