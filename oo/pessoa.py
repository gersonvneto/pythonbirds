class Pessoa:  # criar seus types personalizados
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar()) # executando passando o próprio obj

##Obs.: método nada mais é que uma função que pertence a uma classe
# portanto, sem estar conectada a um objeto

