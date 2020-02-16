# Exercicio 1
DiaSem = input("Dia da semana: ")
if DiaSem == "Domingo" or DiaSem == "Sabado":
    print("Hoje é dia de descanso")
else:
    print("Você precisa trabalhar")
print("\n")
    
# Exercicio 2
lista = ["Banana","Maça","Mamão","Morango","Abacaxi"]
cont = 0
for i in lista:
    if i == "Morango":
        cont += 1;
if cont >= 1:
    print("Morango faz parte da lista")
else:
    print("Morango não faz parte da lista")
print("\n")

# Exercicio 3
tupla = (2,4,6,8)
lista = []
mult = 0;
for i in tupla:
    mult = i*2  
    lista.append(mult)
print(lista)
print("\n")

# Exercicio 4
for i in range(100,151,2):
    print(i)
print("\n")

# Exercicio 5
temperatura = 40  
while temperatura > 35: 
    print(temperatura)
    temperatura = temperatura - 1
print("\n")

# Exercicio 6
cont = 0
while cont < 100:
    cont +=1
    if cont == 23:
        break
    else:
        print(cont)
print("\n")

# Exercicio 7
lista = []
num = 4
while (num <= 20):
    if (num % 2 == 0):
        lista.append(num)
    num +=1
print(lista)
print("\n")

# Exercicio 8
nums = range(5, 45, 2)
print(list(nums))
print("\n")

# Exercicio 9
temperatura = float(input("Qual a temperatura? "))
if (temperatura > 30):
    print("Vista roupas leves.")
else:
    print("Busque seus casacos.")
print("\n")

# Exercicio 10
frase = "É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a vantagem de existir."
cont = 0
for i in frase:
    if i == 'r':
        cont += 1;
print(cont);
print("\n")