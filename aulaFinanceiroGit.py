# -*- coding: UTF-8 -*-
def calculaINSS (salarioBruto):
    if salarioBruto <=1000:
        return 0.0
    if salarioBruto <=2000:
        valINSS = salarioBruto*0.10
        return valINSS
    else:
        valINSS = salarioBruto*0.20
        return valINSS

def calculaIR (salarioLiquido, valINSS):

    return

valSalarioBruto = input ("Entre com o valor do seu salario bruto: ")
qtdDependentes = input ("Quantos dependentes você tem? ")
print calculaINSS(valSalarioBruto)
print qtdDependentes
