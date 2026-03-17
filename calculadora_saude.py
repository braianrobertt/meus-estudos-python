# O comando 'input' faz o computador exibir uma pergunta e esperar você digitar
nome = input("Qual é o seu nome? ")
peso_atual = float(input(f"Olá {nome}, qual é o seu peso atual em kg? "))
altura = float(input("Qual a sua altura").replace(',', '.'))
# Fazendo o cálculo baseado no que você digitou
proteina_ideal = peso_atual * 2
IMC = peso_atual / (altura * altura)

print("\n--- RESULTADO PERSONALIZADO ---")
print(f"Muito bem, {nome}!")
print(f"Para manter sua meta de hipertrofia, consuma {proteina_ideal}g de proteína hoje.")
print(f"seu Indice de Massa Corporal é {IMC:.0F}")
