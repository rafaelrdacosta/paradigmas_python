from class_livro import livro

class biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []

    def adicionar_livros(self, livro):
        self.livros.append(livro)
        print(f'Livro "{livro.titulo}" adicionado à biblioteca "{self.nome}"')

    def remover_livros(self, isbn):
        for livro in self.livros:
            if livro.isbn == isbn:
                self.livros.remove(livro)
                print(f'Livro "{livro.titulo}" removido da biblioteca "{self.nome}"')
                return
        print(f'Livro com ISBN {isbn} não encontrado na biblioteca {self.nome}')

    def listar_livros(self):
        if not self.livros:
            print(f'A biblioteca "{self.nome}" não tem livros.')
        else:
            print(f'Livros na biblioteca "{self.nome}":')
            for livro in self.livros:
                print(f'- {livro.titulo} por {livro.autor} (ISBN: {livro.isbn})')

    def buscar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                print(f'Livro:\nTítulo: {livro.titulo}\nAutor: {livro.autor}\nISBN: {livro.isbn}')
                return livro
        print(f'Livro com Título "{titulo}" não foi encontrado na biblioteca {self.nome}')
        return None