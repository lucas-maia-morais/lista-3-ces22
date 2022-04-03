import q_1_abstrato

class Chocolate:
    
    __drops = 0
    __barras = 0

    def __init__(self, formato, ingrediente):
        '''Inicialização de qualquer chocolate'''
        self.formato = formato
        self.ingrediente = ingrediente

    # Metodo de classe facilita a implementação de novos objetos
    @classmethod
    def barra(cls, ingrediente):
        '''Criação de chocolates do tipo barra'''
        Chocolate.__barras += 1
        return cls(q_1_abstrato.Retangulo(9, 12), ingrediente)
    
    @classmethod
    def drop(cls, ingrediente):
        '''Criação de chocolates do tipo drop'''
        Chocolate.__drops += 1
        return cls(q_1_abstrato.Circulo(3), ingrediente)

    # O método estático assim como em outra linguagem ajuda no acesso de alguma informação que está escondida na classe.
    # Neste caso temos um contador para cada tipo de chocolate implementado e precisamos retornar a quantidade de tipos.
    @staticmethod
    def number(type):
        '''Retorna o numero de chocolates de um tipo'''
        try:
            d = {'drop': Chocolate.__drops, 'barra': Chocolate.__barras}
            return d[type]
        except:
            return 0

    def __str__(self) -> str:
        return 'Chocolate formato {0} sabor {1}'.format(self.formato, self.ingrediente)


def main():
    b1 = Chocolate.barra('Dark')
    b2 = Chocolate.barra('Branco')
    b3 = Chocolate.barra('Ao Leite')
    d1 = Chocolate.drop('Menta')
    d2 = Chocolate.drop('Laranja')

    print(b1)
    print(b2)
    print(b3)
    print(d1)
    print(d2)
    print('\n\n')
    type1 = 'barra'
    type2 = 'drop'
    type3 = 'praline'
    print('Numero de chocolates {0} {1}'.format(type1, Chocolate.number(type1)))
    print('Numero de chocolates {0} {1}'.format(type2, Chocolate.number(type2)))
    print('Numero de chocolates {0} {1}'.format(type3, Chocolate.number(type3)))


if __name__ == '__main__':
    main()