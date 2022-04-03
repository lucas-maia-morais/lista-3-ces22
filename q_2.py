class A():
    def __init__(self):
        self.param = []
        self.param_dict = {}


    @property
    def parametros(self):
        for p in self.param:
            print('Value: {0}'.format(p))

        for key, p in self.param_dict.items():
            print('Key: {0} value: {1}'.format(key, p))

    @parametros.setter
    def parametros(self, *args):
        if (type(args[0]) == tuple) or (type(args[0]) == list) or (type(args[0] == range)):
            self.param = args[0]
            self.param_dict = {}
        if (type(args[0]) == dict):
            self.param_dict = args[0]
            self.param = []

def main():
    a = A()
    a.parametros = {'Teste': '1', 'Casa': 'Nova', 'Hello': 'World!'}
    a.parametros
    a.parametros = range(5)
    a.parametros
    a.parametros = {'Power': 'Rangers', 'Tesla': 'Space X', 'Bill': 'Gates'}
    a.parametros
    a.parametros = 8,1,3,5,'queijo'
    a.parametros

if __name__ == '__main__':
    main()