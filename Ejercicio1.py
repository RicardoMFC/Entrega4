lista = ["El Padrino","Apocalypse Now","La ley del silencio"]
tupla = ('El buscavidas','La leyenda del indomable', 'El golpe')
print(lista)
print(tupla,"\n")

print(lista[1])
print(tupla[-2],"\n")

lista[1]= 'La jauría humana'
print (lista,"\n")
#No se pueden cambiar los elementos de las tuplas

print("La lista tiene {} elmentos y la tupla {}\n".format(len(lista),len(tupla)))

#Recorro todas las posiciones de lista, si en alguna pone La jauría humana, el valor cambia a 1 y sale del while.
i=0
while i<=len(lista):
  if lista[i]=='La jauría humana':
    print("Este elemento aparece en la posición {}".format(i))
    break
  i+=1
#Otra forma de hacerlo
print('La jauría humana' in lista,"\n")

lista+=['Un tranvía llamado deseo', 'Julio César']
#lista.append('Un tranvía llamado deseo'), solo para añadir un elemento.
tupla+=('Dos hombres y un destino', 'El color del dinero')
#tupla.append('Dos hombres y un destino'), la función .append no se puede utilizar con la tupla.
print(lista)
print(tupla,"\n")

#Con la función pop o remove podemos eliminar los elementos de la lista que queramos, con pop indicamos la posición que se quiere eliminar y con remove el contenido de la posición que se quiere eliminar. 
lista.pop(0)
print(lista)
lista.remove('La jauría humana')
print (lista)
#Para las tuplas no se hay ninguna función predefinida que permita elimiar alguna posición.