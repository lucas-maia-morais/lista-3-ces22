from abc import ABC, abstractmethod
from math import radians
import math

# A ideia de utilizar funções abstratas é criar metodos comuns a todas as subclasses, porém que devem ser feitas individualmente
# com as propriedades daquele objeto, observando o caso a seguir temos por exemplo que initializar cada figura geométrica com suas
# proprias caracteristicas, porém gostariamos que cada uma delas retornasse a area dessa figura e a maior distancia entre pontos,
# ao invés de individualmente confiar na habilidade do programador é mais interessante criar o método abstrato como forma de uniformizar
# subclasses e evitar esquecimentos.
# Observação de método abstrato é independente de métodos de instância, de classe, e estáticos, portanto podemos ter métodos abstratos
# desses tipos.
class FigurasGeometricas(ABC):
    @abstractmethod
    def __init__(self):
        '''Construtor adequado para cada classe de figura geométrica'''
        pass

    @abstractmethod
    def maior_distancia(self):
        '''Função que retorna  a maior distância de um objeto'''
        pass

    @abstractmethod
    def area(self):
        '''Função que retorna a area de um objeto'''
        pass

class Circulo(FigurasGeometricas):

    def __init__(self, raio):
        self.raio = raio

    def maior_distancia(self):
        return 2*self.raio

    def area(self):
        return math.pi * self.raio * self.raio
    
    def __str__(self) -> str:
        return 'Circulo de raio {0}'.format(self.raio)

class PoligonoRegular(FigurasGeometricas):
    def __init__(self, pontos, lado):
        self.pontos = pontos
        self.lado = lado

    def area(self):
        return self.pontos * self.lado * self.lado /( 4 *  math.tan(math.pi/self.pontos) )
    
    def maior_distancia(self):
        if self.pontos == 3:
            return self.lado
        elif self.pontos % 2 == 0:
            return self.lado / math.sin(math.pi/self.pontos)
        else:
            return self.lado / ( 2 * math.sin( math.pi / (2 * self.pontos) ) )

    def __str__(self) -> str:
        return 'Poligono regular de {0} lados e lado {1}'.format(self.pontos, self.lado)

class Retangulo(FigurasGeometricas):
    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2
    
    def area(self):
        return self.l1 * self.l2

    def maior_distancia(self):
        return math.sqrt( self.l1 ** 2 + self.l2 ** 2)

    def __str__(self) -> str:
        return 'Retangulo {0}x{1}'.format(self.l1, self.l2)

def main():
    c = Circulo(5)
    print(c.area())
    print(c.maior_distancia())
    p = PoligonoRegular(5, 1)
    print(p.area())
    print(p.maior_distancia())
    r = Retangulo(3, 4)
    print(r.area())
    print(r.maior_distancia())

if __name__ == '__main__':
    main()