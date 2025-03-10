nome = input("Inserir o nome e sobrenome do cadastrador: ")
print(f"Bem-vindo ao sistema de vendas!  {nome}")  

valor_unitario = float(input("Digite o valor unitário do produto: "))  
quantidade = int(input("Digite a quantidade desejada: "))

valor_total = valor_unitario * quantidade 

if valor_total < 2500:  
    desconto = 0
elif valor_total >= 2500 and valor_total < 6000:
    desconto = 0.04  # 4%
elif valor_total >= 6000 and valor_total < 10000:
    desconto = 0.07  # 7%
else:
    desconto = 0.11  # 11%

valor_desconto = valor_total * desconto
valor_final = valor_total - valor_desconto

print(f"\nValor total sem desconto: R$ {valor_total:.2f}")
print(f"Desconto aplicado: {desconto * 100:.0f}%")
print(f"Valor total com desconto: R$ {valor_final:.2f}")

if valor_total >= 2500:  
    print("Seu pedido recebeu um desconto especial!")