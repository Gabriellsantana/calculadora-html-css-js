def soma(a, b):
    return a + b
def subtracao(a, b):
    return a - b
def multiplicacao(a, b):
    return a * b
def divisao(a, b):
    if b != 0:
        return a/b
    else:
        return "erro divisão por zero"
print("SELECIONE A OPERAÇÃO: ")
print("1 - soma")
print("2 - subtração")
print("3 - mutiplicação")
print("4 - divisão")
operacao = input('Digite o numero da operação aqui : ')
n1 = float(input("Digite um Numero: "))
n2 = float(input("Digite outro Numero: "))
if operacao =='1':
    print(n1, ' + ', n2, '=', soma(n1, n2))
elif operacao =='2':
    print(n1, ' - ', n2, '=', subtracao(n1, n2))
elif operacao == '3':
    print(n1, ' x ', n2, '=', multiplicacao(n1, n2))
elif operacao == '4':
    print(n1, ' % ', n2, '=', divisao(n1, n2))
else:
    print('###[operação inválida]####')


