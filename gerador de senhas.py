import random
maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
minusculas ="abcdefghijklmnopqrstuvwxyz"
numeros ="0123456789"
caracteres_especiais ="{}[]()*:;?.,_-"
tudo = maiusculas+minusculas+numeros+caracteres_especiais
tamanho = int(input("Diga qual tamanho a senha deve ter: "))
senha = " ".join(random.sample(tudo,tamanho))
print(senha)