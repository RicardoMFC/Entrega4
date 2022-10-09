#Ejercicio3
lista=[]
x=int (input("Indique el tamaño de la lista\n"))
for i in range(x):
  lista.append(float(input("Escriba un numero\n")))
print("\n{}\n".format(lista))
sumatorio=sum(lista)
print("sumatorio = {}\n".format(sumatorio))

#Otra forma de sumar los elementos, sin la función sum.
sum=0
for j in range(x):
  sum+=lista[j]

print(sum==sumatorio,"\n")
#En el ejercicio3 definimos la lista vacía, leemos por teclado el tamaño de la lista y mediante un bucle for vamos rellenando la lista, a través de la función append. Después, con la función predefinida sum, sumamos sus elementos.

#Ejercicio4
media_arit=sum/x
print ("Media aritmetica = {}".format(media_arit))
#Simplemente dividimos el sumatorio entre x, que es el tamaño de la lista.