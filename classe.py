import math


class Retangulo():

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def getBase(self):
        return self.base

    def getAltura(self):
        return self.altura

    def calcArea(self):
        return self.base * self.altura

    def calcPerimetro(self):
        return 2 * (self.altura + self.base)

    def calcDiagonal(self):
        return math.sqrt(self.base ** 2 + self.altura ** 2)
