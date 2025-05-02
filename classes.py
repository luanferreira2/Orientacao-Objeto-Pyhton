import math
from abc import ABC, abstractmethod

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


class Pessoa(ABC):
    def __init__(self, nome, anoInscricao, totalCompras):
        self.nome = nome
        self.anoInscricao = anoInscricao
        self.totalCompras = totalCompras

    @abstractmethod
    def calcBonus(self, anoInscricao):
        pass

    def addCompras(self, valor):
        self.totalCompras += valor

    def getNome(self):
        return self.nome

    def getAnoInscricao(self):
        return self.anoInscricao

    def getTotalCompras(self):
        return self.totalCompras

class PessoaJuridica(Pessoa):

    def __init__(self, nome, anoInscricao, totalCompras, cgc, taxaIncentivo):

        super().__init__(nome, anoInscricao, totalCompras)
        self.cgc = cgc
        self.taxaIncentivo = taxaIncentivo

    def getTaxaIncentivo(self):
        return self.taxaIncentivo
    def getCgc(self):
        return self.cgc
    def calcBonus(self, anoAtual):
        return ( self.getTaxaIncentivo() / 100 * self.getTotalCompras()) * (anoAtual - self.getAnoInscricao())


class PessoaFisica(Pessoa):

    def __init__(self, nome,  anoInscricao, totalCompras, cpf, base):
        super().__init__(nome, anoInscricao, totalCompras)
        self.cpf = cpf
        self.base = base

    def calcBonus(self, anoAtual):

        bonus = 0

        if (self.getTotalCompras() > 12000):

         bonus = (anoAtual - self.getAnoInscricao()) * self.getBase()

        return bonus

    def getCpf(self):
        return self.cpf

    def getBase(self):
        return self.base
