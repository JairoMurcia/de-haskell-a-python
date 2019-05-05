def suma(a,b):
    return a+b

def resta(a,b):
    return a-b


def division(a,b):
    if b==0:
        return None
    else:
        return a/b        
def producto(a,b):
    return a*b



def factorial(x):
    if x==0:
        return 1
    else:
        return x*factorial(x-1)


def fibonacci(a):
    if a==0:
        return 0
    elif a==1:
        return 1
    else:
        return fibonacci(a-1)+fibonacci(a-2)        


def cuadrado(x):
    return x**2

def potencia(a,b):
    if b==0 or a==1:
        return 1
    else:
        return  a*potencia(a,b-1)

def suma_digitos(a):
    if a<10:
        return a
    else:
        return suma_digitos(a//10)+a%10    

def diezADos(a):
    if a <2:
        return a
    else:
        return a%2 +diezADos(a//2)*10    
def dosADiez(a):
    if a<2:
        return  a
    else:
        return  a%10 +dosADiez(a//10)*2 
def siguiente(a):
    if a>9:
        return 1
    else:
        return a+1

def anterior(a):
    if a<1:
        return 9
    else:
        return a-1


def suma_lista(y):
    if len(y)==1 :
        return y[0]
    elif len(y)!=0:
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

def doblar(x):
    if len(x)==1:
        return [x[0]*2]
    else:
        return [x[0]*2]+cuadrado(x[1:])   

def ultimo_elemento(x):
    if len(x)==1 or len(x)==0:
        return x
    else:
        return ultimo_elemento(x[1:])    

def cuadrado(x):
    if len(x)==1:
        return [x[0]**2]
    else:
        return [x[0]**2]+cuadrado(x[1:])    


