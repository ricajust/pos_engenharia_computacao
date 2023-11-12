print("IMC\n")

peso = float(input("Entre com o peso: "))
altura = float(input("Entre com a altura: "))

#peso /altura * altura
imc = round(peso / altura * altura, 2)

print(f"\nO IMC é: {imc}")

if imc >= 26:
	print("Está acima do peso ideal")
else:
	print("Está dentro do padrão")