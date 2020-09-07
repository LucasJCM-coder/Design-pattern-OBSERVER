
class Roubado: 
    def __init__(self, observador=''):
        self.sub = observador

    def subscribe(self, observador):
        self.sub = observador

    def notificy(self, acao):
        self.sub.update(acao)

    def direita(self):
        print("Carro roubado virou a direita")
        self.notificy('direita')

    def esquerda(self):
        print("Carro roubado virou a esquerda")
        self.notificy('esquerda')

    def frente(self):
        print("Carro roubado seguiu em frente")
        self.notificy('frente')
        
    def parar(self):
        print("Carro roubado parou")
        self.notificy('parar')

    def re(self):
        print('Carro roubado deu a ré')
        self.notificy('re')

class Policia:
    def direita(self):
        print("VIATURA virou a direita")
        
    def esquerda(self):
        print("VIATURA virou a esquerda")

    def frente(self):
        print("VIATURA seguiu em frente")

    def parar(self):
        print("VIATURA parou")

    def update(self, acao):
        acoes = {
            'parar': self.parar,
            'frente': self.frente,
            'direita': self.direita,
            'esquerda': self.esquerda,
            }
        if acao in acoes:
            acoes[acao]()
        
if __name__ == '__main__':
    policia = Policia()
    ladrao = Roubado()

    ladrao.subscribe(policia)

    ladrao.re()