vet=[]
pares=[]
for i in range(0,11,1):#posição inicial é o ponto de partida,segunda posição igual a ir até essa posição menos um,ultima posição incrementa 1
    vet.append(i+10)
    if(vet[i]%2==0):
      pares.append(vet[i])
    print("Vetor Original:",vet)
pares_Decresc=pares
for j in range(1,len(pares)):
    for i in range(0,j):
        if(pares_Decresc[j] >= pares_Decresc[i]):
           aux=pares_Decresc[j]
           pares_Decresc[j]=pares_Decresc[i]
           pares_Decresc[i]=aux
print("Vetor ordem Decrescente",pares_Decresc)
 