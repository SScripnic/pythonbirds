class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão'

class Mutante(Pessoa):
    olhos = 3

if __name__ == "__main__":
    sergio = Mutante(nome='Sergio')
    alexandre = Homem(sergio, nome='Alexandre')
    print(Pessoa.cumprimentar(alexandre))
    print(id(alexandre))
    print(alexandre.cumprimentar())
    print(alexandre.nome)
    print(alexandre.idade)
    for filho in alexandre.filhos:
        print(filho.nome)
    alexandre.sobrenome = 'Ribeiro'
    del alexandre.filhos
    print(alexandre.__dict__)
    print(sergio.__dict__)
    print(Pessoa.olhos)
    print(sergio.olhos)
    print(id(Pessoa.olhos), id(alexandre.olhos), id(sergio.olhos))
    print(Pessoa.metodo_estatico(), alexandre.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), alexandre.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(sergio, Pessoa))
    print(isinstance(sergio, Homem))
    print(sergio.olhos)
    print(alexandre.cumprimentar())
    print(sergio.cumprimentar())