n=int(input("Indique el tamaño de la lista\n"))
i=0
sum=0
lista=[]
while i<n:
  x=float(input("Indique un numero\n"))
  lista[i]=x
  sum+=x
  i+=1
print (sum)