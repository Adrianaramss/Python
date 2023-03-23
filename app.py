# testando variavel nome 
nome = "Poliana"
print ("olá", nome, "seja bem - vinda")

#testando soma 
numero = 1
print (numero + 2)


limiar = 5 
menores = [] #criar lista menores
maiores = [] # criar lista maiores
for  i in range (10):
    if (i < limiar):
        menores.append(i)
    elif (i > limiar):
        maiores.append(i)


print ("resultado final")
print("maiores" , maiores)
print ("menores", menores)