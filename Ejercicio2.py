set = {"Martin Scorsese", "Sergio Leone", "Francis Ford Coppola"}
vehiculo = {
  "marca":"Aston Martin",
  "modelo":"Valkyrie",
  "año":2022
} 

print (set)
print (vehiculo)

print ("\n",vehiculo["modelo"],"\n")
#En los set los elmentos no están ordenados por lo que no podemos mostrar el segundo elemento del set refiriéndonos a él con un índice.

#En el set no se puede cambiar sus elementos, pero podemos añadir un nuevo elemento y eliminar otro.
set.add("Steven Spielberg")
set.remove("Sergio Leone")
print (set)
#En los diccionarios se pueden cambiar los valores haciendo referencia a sus claves 
vehiculo["año"]=2020
print (vehiculo,"\n")

print ("El tamaño del set es {} y el del diccionario {}\n".format(len(set),len(vehiculo)))

print('Martin Scorsese' in set)
print ("marca" in vehiculo,"\n")

set.add("Sergio Leone")
vehiculo[""]="AMR Pro"
print (set)
print (vehiculo,"\n")

set.remove("Steven Spielberg")
print (set)
#Con popitem eliminamos el último elemento del diccionario
vehiculo.popitem()
print (vehiculo)
#Con pop eliminamos el elemento de clave seleccionado
vehiculo.pop("año")
print(vehiculo)
#Con clear eliminamos todos los elementos del diccionario
vehiculo.clear()
print(vehiculo)

