class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


if __name__ == "__main__":
    sergio = Pessoa(nome='Sergio')
    alexandre = Pessoa(sergio, nome='Alexandre')
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