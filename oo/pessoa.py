class Pessoa:  # criar seus types personalizados
    def __init__(self, *filhos, nome = None, idade = 35):  # atributos de dados
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    renzo = Pessoa(nome='Renzo')
    luciano = Pessoa(renzo, nome = 'Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar()) # executando passando o próprio obj
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)

##Obs.: método nada mais é que uma função que pertence a uma classe
# portanto, sempre está conectada a um objeto



