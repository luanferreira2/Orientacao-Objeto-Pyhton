from classes import PessoaFisica, PessoaJuridica

anoAtual = int(input(' Digite o Ano Atual: '))

nomePF = input(' Digite o nome da Pessoa Fisica: ')
anoInsc = int(input(' Digite o ano de inscrição: '))
totalCompras = 0
cpf = input(' Digite o CPF: ')
salBase = float(input(' Digite o Salário Base: '))

pessoaF = PessoaFisica(nomePF, anoInsc, totalCompras, cpf, salBase)

pessoaF.addCompras(5500)
pessoaF.addCompras(2050)
pessoaF.addCompras(5000)

print('\n')

print(f' CPF: {pessoaF.getCpf()}')
print(f' Nome: {pessoaF.getNome()}')
print(f' Ano de Inscrição: {pessoaF.getAnoInscricao()}')
print(f' Salário Base: R$ {pessoaF.getBase()}')
print(f' Total de Compras: {pessoaF.getTotalCompras()}')
print(f' Bonus: {pessoaF.calcBonus(anoAtual)}')


nomePJ = input(' Digite o Nome da Pessoa Jurídica: ')
anoInsc = int(input(' Digite o Ano de Inscrição: '))
anoAtual = int(input(' Digite o Ano Atual: '))
totalCompras = 0
cgc = int(input(' Digite o CGC: '))
taxaIncentivo = float(input(' Digite a Taxa de Incentivo: '))

pessoaJ = PessoaJuridica(nomePJ, anoInsc, totalCompras, cgc, taxaIncentivo)

pessoaJ.addCompras(7600)
pessoaJ.addCompras(1450)
pessoaJ.addCompras(4900)

print('\n')

print(f' CGC: {pessoaJ.getCgc()}')
print(f' Nome: {pessoaJ.getNome()}')
print(f' Ano de Inscrição: {pessoaJ.getAnoInscricao()}')
print(f' Taxa de Incentivo: {pessoaJ.getTaxaIncentivo()}')
print(f' Total de Compras: {pessoaJ.getTotalCompras()}')
print(f' Bonus: {pessoaJ.calcBonus(anoAtual)}')
