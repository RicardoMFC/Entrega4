#la diferencia entra un lista y una dupla, es que en la lista podemos cambiar los elementos y en la dupla no. La dupla va entra paréntesis y la lista entre corchetes
lista = ["El Padrino","Apocalypse Now","La ley del silencio"]

tupla = ('El buscavidas','La leyenda del indomable', 'El golpe')
print(lista)
print(tupla)

print(lista[1])
print(tupla[-1])

lista[1]= 'La jauría humana'
print (lista)
#No se pueden cambiar los elementos de las tuplas

print("La lista tiene {} elmentos".format(len(lista)))
print("La tupla tiene {} elmentos".format(len(tupla)))

#Recorro todas las posiciones de lista, si en alguna pone La jauría humana, el valor cambia a 1 y sale del while.
i=0
while i<=len(lista):
  val=0
  if lista[1]=='La jauría humana':
    val=1
    break
  i+=1
print(val)
#Otra forma de hacerlo
print('La jauría humana' in lista)

lista+=['Un tranvía llamado deseo', 'Julio César']
#lista.append('Un tranvía llamado deseo'), solo para añadir un elemento.
tupla+=('Dos hombres y un destino', 'El color del dinero')
#tupla.append('Dos hombres y un destino'), la función .append no se puede utilizar con la tupla.
print(lista)
print(tupla)
#Con la función pop o remove podemos eliminar los elementos de la lista que queramos, con pop indicamos la posición que se quiere eliminar y con remove el contenido de la posición que se quiere eliminar. 
lista.pop(0)
print(lista)
lista.remove('La jauría humana')
print (lista)

#Para las tuplas no se hay ninguna función predefinida que permita elimiar alguna posición.
j=0
while j<=len(lista):
  if lista[j]=='Un tranvía llamado deseo':
    lista[j]=='h'
    break
  j+=1
print (lista)
