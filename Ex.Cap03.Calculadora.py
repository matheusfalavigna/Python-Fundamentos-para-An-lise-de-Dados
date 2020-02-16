#Calculadora 
def soma(num1, num2):
        print("Soma: ",num1 + num2)
        return
def sub(num1, num2):
        print("Subtração: ",num1 - num2)
        return
def mult(num1, num2):
        print("Multiplicação: ",num1 * num2)
        return
def div(num1, num2):
        print("Divisão: ",num1 // num2)
        return
    
print("Selecione a opção de calculo desejado:\n")

print("1 - Soma\n")
print("2 - Subtração\n")
print("3 - Multiplicação\n")
print("4 - Divisão\n")

x = int(input("Digite o valor entre (1/2/3/4):\n"))

num1 = int(input("Digite o 1º valor: \n"))
num2 = int(input("Digite o 2º valor: \n"))

if x == 1:
    soma(num1, num2)
elif x == 2:
    sub(num1, num2)
elif x == 3:
    mult(num1, num2)
else:
    div(num1, num2)    