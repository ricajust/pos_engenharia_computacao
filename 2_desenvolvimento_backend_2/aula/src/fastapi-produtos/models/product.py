from pydantic import BaseModel #no django importamos o models.Model aqui usamos esse BaseModel

class Product(BaseModel):
	"""
	id, name, description, price
	"""

	id: int
	name: str
	description: str
	price: float