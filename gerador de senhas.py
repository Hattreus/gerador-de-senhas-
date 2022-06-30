import random
maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
minusculas ="abcdefghijklmnopqrstuvwxyz"
numeros ="0123456789"
caracteres_especiais ="{}[]()*:;?.,_-"
tudo = maiusculas+minusculas+numeros+caracteres_especiais
tamanho = 8
senha = "".join(random.sample(tudo,tamanho))
print(senha)