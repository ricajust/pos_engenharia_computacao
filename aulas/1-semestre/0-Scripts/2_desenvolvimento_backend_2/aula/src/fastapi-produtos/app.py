from fastapi import FastAPI #importa o fastAPI
from models.product import Product #importa da classe Product

app = FastAPI() #cria uma instância do fastAPI (semelhante ao Express do NodeJS)

data = [
	Product(id=1, name='Coca-Cola', description='Bebida', price= 9.98),
    Product(id=2, name='Tenis Nike Air', description='Calçados', price=799.99),
    Product(id=3, name='Iphone', description='Tecnologia', price=3998.99),
    Product(id=4, name='Notebook', description='Tecnologia', price=4980.99),
]

@app.get('/')
def say_hello():
	"""
	Exibe uma mensagem de boas vindas
	"""
	return({'Hello': 'World'})

@app.get('/{name}')
def say_hello(name:str):
	"""
	Exibe uma mensagem de boas vindas com um nome digitado na URL
	"""
	if(not name):
		pass
	else:
		return({'Hello': name})

@app.get('/api/exibir_produtos')
def show_all_products():
	"""
	Exibe todos os produtos cadastrados
	"""
	return (data)

@app.get('/api/exibir_produto/{id}')
def show_product(id:int):
	"""
	Exibe um único produto por id
	"""
	if (not id):
		pass
	else:
		return data[id-1]
