class A:
    def nada(self):
        print('O nada de A1 é nada1')
        return 'nada'
    
class B(A):
    def nada(self):
        print('O nada de B é rien')
        print('O nada herdado de B é {0}'.format(super(B, self).nada()))
        return 'rien'

class C(A):
    def nada(self):
        print('O nada de C é nothing')
        print('O nada herdado de C é {0}'.format(super(C, self).nada()))
        return 'nothing'

# Seguindo a ideia de method resolution order para python, ele sempre segue o super da classe mais a esquerda a mais a direita, fazendo uma busca em largura.
class D(B,C):
    def nada(self):
        print('O nada herdado de D é {0}'.format(super(D, self).nada()))


def main():
    d = D()
    d.nada()

if __name__ == '__main__':
    main()