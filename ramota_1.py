def suma(inp1,inp2):
    suma= inp1+inp2 
    return suma
print('escribe un numero')
ent1= int(input())
ent2= int(input())
print (suma(ent1,ent2))

edad=int (input('cual es tu edad: '))
color= str(input('cual es tu colo favorito: '))
random= 'tu edad es {} y  tu color favorito es {} '.format(edad,color)
print(random)
random1= f'tu edad es {edad} y  tu color favorito es {color} '
print (random1)