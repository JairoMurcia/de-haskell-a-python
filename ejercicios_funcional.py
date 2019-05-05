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
    elif a[0]==b[0] and len(a)==len(b):
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
    
def invertir(x):
	if len(x)==1:
		return [x[0]]
	else:
		return [x[len(x)-1]]+invertir(x[:len(x)-1])	


print(invertir([1,2,3,4,5,6]))	
