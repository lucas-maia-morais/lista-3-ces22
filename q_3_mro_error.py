# Caso em que o mro falha ao tentar construir uma ordem de percorrer as classes

class A1:
    def nada(self):
        print('O nada de A1 é nada1')
        return 'nada'

class A2:
    def nada(self):
        print('O nada de A2 é nada2')
        return 'nada'
    
class B(A1,A2):
    def nada(self):
        print('O nada de B é rien')
        print('O nada herdado de B é {0}'.format(super(B, self).nada()))
        return 'rien'

class C(A2,A1):
    def nada(self):
        print('O nada de C é nothing')
        print('O nada herdado de C é {0}'.format(super(C, self).nada()))
        return 'nothing'

# Seguindo a ideia de method resolution order para python, ele sempre segue o super da classe mais a esquerda a mais a direita, fazendo uma busca em largura.
# Neste caso há um erro de consistencia, pois o mro não sabe se segue da direita D, B (da decl de D), C (da decl de D), A1(da decl de B),
# A2(da decl de B) ou D, B (da decl de D), C (da decl de D), A1(da decl de C), ou A2(da decl de C)
class D(B,C):
    def nada(self):
        print('O nada herdado de D é {0}'.format(super(D, self).nada()))


def main():
    d = D()
    d.nada()

if __name__ == '__main__':
    main()