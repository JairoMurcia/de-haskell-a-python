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
    
def invertir_lista(a,b):
    if len(a)==2:
        b.append(a[0])
        return b
    else:
        b.append(a[len(a)-1])
        return invertir_lista(a[:len(a)],b)

a=[1,3,5,4,3,5,8]
b=[1]


print(invertir_lista(a,[]))
