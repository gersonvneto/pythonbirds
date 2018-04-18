class Pessoa:  # criar seus types personalizados
    def __init__(self, nome = None, idade = 35):  # atributos de dados
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Luciano')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar()) # executando passando o próprio obj
    print(p.nome)
    p.nome = 'Renzo'
    print(p.nome)
    print(p.idade)


##Obs.: método nada mais é que uma função que pertence a uma classe
# portanto, sempre está conectada a um objeto



