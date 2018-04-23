class Pessoa:  # criar seus types personalizados
    olhos = 2   # atributo default ou de classe

    def __init__(self, *filhos, nome = None, idade = 35):  # atributos de dados
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42     #fazer algum cálculo que independa da classe e objeto se nao for no
                      # metodo estatico

    @classmethod
    def nome_e_atributos_de_classe(cls):  # usado para acessar dados da propria classe
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão'
# super() vai chamar os elementos da classe pai
class Mutante(Pessoa):
    olhos = 3
    #sobrescrita de atributo de dados

if __name__ == '__main__':
    renzo = Mutante(nome='Renzo')  # podemos mudar para homem e continuamos a obter o mesmo result, pq homem herdou de pessoa
    luciano = Homem(renzo, nome = 'Luciano')
    print(Pessoa.cumprimentar(luciano))   # obrigado a passar o objeto
    print(id(luciano))
    print(luciano.cumprimentar()) # executando passando o próprio obj
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome = 'Ramalho'
    print(luciano.sobrenome)
    print(luciano.__dict__)
    print(renzo.__dict__)  #mostra os atributos (criados anteriormente e on the fly)
    del luciano.filhos  # remove atributos
    luciano.olhos = 1
    del luciano.olhos
    print(Pessoa.olhos)  # faz sentido porque é um default atributo de classe
    print(luciano.olhos)
    print(renzo.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(renzo.olhos))  # sao iguais
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico()) # sem o obj dentro(1 arg pq e e estat) ou atraves do obj
                                                               # se o atributo nao for encontrado no obj,
                                                               # o python procura na classe(2 arg)
    print(Pessoa.nome_e_atributos_de_classe(), luciano.nome_e_atributos_de_classe())
    # pode ser executado pela classe ou pelo objeto

    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(renzo, Homem))
    print(isinstance(renzo, Pessoa))
    print(renzo.olhos)
# quando uma classe nao herda de nenhuma outra, ela herda implicitamente da classe raiz object
# e a busca vai pesquisar se há o atributo no object se nao encontrar em nenhuma
    print(luciano.cumprimentar())
    print(renzo.cumprimentar())


##Obs.: método nada mais é que uma função que pertence a uma classe
# portanto, sempre está conectada a um objeto
##Obs2.: podemos criar atributos on the fly para aquele objeto específico(não é boa pratica)



