class Pecas:
    def __init__(self, tipo, cor, local, first = False):
        self.tipo = tipo
        self.cor = cor
        self.local = local
        if tipo == "peao":
            self.first = not first


    

