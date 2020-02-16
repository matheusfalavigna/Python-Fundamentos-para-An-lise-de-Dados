# Exercicio 1
def pares():
    for i in range(2, 21, 2):
        print(i)
print(pares())
print("\n")  

# Exercicio 2
def mai(string):
    print(string.upper())
    return 
string = "adoleta lepeti peti pola"
mai(string)
print("\n") 

# Exercicio 3
def imprimi(lista):
    print(lista.append(5))
    print(lista.append(6))
lista = [1, 2, 3, 4]
imprimi(lista)
print(lista)
print("\n") 

# Exercicio 4
def func(arg, *lista):
    print(arg)
    for i in lista:
        print(i)
    return
arg = 1
func(arg)
lista = [1, 2, 3, 4]
func(lista)
print("\n") 

# Exercicio 5
soma = lambda num1, num2: num1 * num2
num1 = 2
num2 = 4
print(soma(num1, num2))
print("\n") 

# Exercicio 6
total = 0
def soma( arg1, arg2 ):
    total = arg1 + arg2; 
    print ("Dentro da função o total é: ", total)
    return total;
soma( 10, 20 );
print ("Fora da função o total é: ", total)
print("\n") 

# Exercicio 7
Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(lambda x: (float(9)/5) * x + 32 , Celsius)
print (list(Fahrenheit))
print("\n") 

# Exercicio 8
disc = {"x1": "Casa", "x2": "Carro", "x3": "Varanda"}
print(dir(disc))
print("\n") 

# Exercicio 9
import pandas
print(dir(pandas))
print("\n") 

# Exercicio 10
import pandas as pd
file_name = "binary.csv"

def retornaArq(file_name):
    df = pd.read_csv(file_name)
    return df.describe()
    
retornaArq(file_name)  
print("\n") 