def factorial(x):
    if x==0:
        return 1
    else:
        return x*factorial(x-1)


def cuadrado(x):
    return x**2


def suma_lista(y):
    if len[y]==1:
        return y[0]
    else:
        return y[0]+suma_lista(y[1:])

def lista_igual(a,b):
    if len(a)==0 and len(b)==0:
        return True
    elif a[0]==b[0]:
        return lista_igual(a[1:],b[1:])
    else:
        return False

def lista_ordenada(a):
    if len(a)==1 or len(a)==0:
        return True
    elif a[0]<=a[1]:
        return lista_ordenada(a[1:])
    else:
        return False



def mostrar_elemento(a,n):
    if n==0:
        return a[0]
    else:
        return mostrar_elemento(a[1:],n-1)

def contar_pares(a):
    if len(a)==1:
        if a[0]%2==0:
            return 1
        else:
            return 0
    elif a[0]%2==0:
        return 1+contar_pares(a[1:])
    else:
        return 0+contar_pares(a[1:])
    
def invertir(ls):
    if ls == []:
        return null
    
    if len(ls) == 1: #Importante: caso base
        return ls    #El caso base ROMPE la recursividad.
    #Se le indica que retorne el ultimo valor de la lista, y le concatene
    #el resultado de la misma funcion enviando la misma lista pero sin
    #ultimo valor (que ya pusimos al inicio)
    return [ls[len(ls) - 1]] + invertir(ls[:-1])

#Se envuelve cualquier resultado en [] para convertirlo en una lista.
#ls[:-1] remueve el ultimo valor de la lista

def divisible(x, y):
	return (x%y==0)

def divisibles(n):
	listaDiv = []
	listaY = []
	y=1
	while y<=n:
		listaY.append(y)
		y+=1
	for i in listaY:
		if(divisible(n,i)):
			listaDiv.append(i)
	return listaDiv

def esPrimo(n):
	return (len(divisibles(n))<=2)

def primos(n):
	lista = []
	x=1
	while x<=n:
		if(esPrimo(x)):
			lista.append(x)
		x+=1
	return lista

print(primos(n=100))

print(invertir([5,4,3,2,1]))
    
os.system("pause")

print(invertir_lista(a,[]))
