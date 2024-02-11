#importa as bibliotecas
import random

print("Acerte o número secreto\n")

# escolha de um número aleatorio entre (1 e 5)
numero_secreto = random.randint(1, 5)

# recebe o palpite do usuario
palpite = int(input("Escolha seu palpite, escolha os números entre 1 a 5: "))

# se o palpite for igual ao secreto acertou, senão errou
if palpite == numero_secreto:
	print(f"Parabêns!!! Você ganhou!!! O número secreto é {numero_secreto}")
else:
	print(f"Que pena, o número secreto é o {numero_secreto}")