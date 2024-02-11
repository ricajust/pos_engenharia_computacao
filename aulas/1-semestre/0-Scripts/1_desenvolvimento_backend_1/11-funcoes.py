#Funções
def oi():
	print("oi")

def soma_sem_argumentos():
	print(1 + 1)


def soma_com_argumentos(x, y):
	print(x + y)
	
def soma_com_argumentos_e_retorno(a, b):
	return(a + b)

#Invocação das funções
oi() # 'oi'
soma_sem_argumentos() # 2
soma_com_argumentos(1, 2) # 3
print(soma_com_argumentos_e_retorno(1, 4)) # 5


