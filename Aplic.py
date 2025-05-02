from classes import Retangulo

base = float(input(' Digite a base do retangulo: '))
altura = float(input('Digite a altura do retangulo: '))

retangulo1 = Retangulo(base, altura)

print(f' A base do retangulo é de: {retangulo1.getBase()}')
print(f'A altura do retangulo é de: {retangulo1.getAltura()}')

print(f' A área do retangulo é de: {retangulo1.calcArea()}')
print(f' O perímetro do retangulo é de: {retangulo1.calcPerimetro()}')
print(f' A diagonal do retangulo é de: {retangulo1.calcDiagonal()}')
