lista = []
contador = 1
opcao = 1

while True:
    lista.append(
        int(input(f"Digite o numero de reféns presos no mês: ")))
    opcao=int(input("Adicionar outro mês? \n não = 0 \n sim = 1\n"))
    contador +=1
    if (opcao == 0 or opcao != 1):
        break

maior = lista [0]
for n in lista:
    if n > maior:
        maior = n
print (f"\nMaior número de capturados: {maior}")

menor = lista [0]
for i in lista:
    if i < menor:
        menor = i
print (f"Menor número de capturados: {menor}")

total_presos = 0
for i in lista:
    total_presos += i
print (f"Total de presos: {total_presos}")

media = total_presos / len(lista)
print ("Média: %.2f" % media)

diffList = []
tamanho = len(lista)
for n in range(tamanho):
    diffList.append(abs(media - lista[n]))

menorAprox = indexMenor = None
for key, value in enumerate(diffList):
    if key == 0:
        menorAprox = value
    else:
        if value < menorAprox:
            menorAprox = value
            indexMenor = key
print(f"O valor aproximado da média de capturados foi de {lista[indexMenor]}")