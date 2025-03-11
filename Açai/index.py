
print(f"Bem-vindo à loja de Açaí e Cupuaçu! Desenvolvido por Ruan Paixão")

precos = {
    "CP": {"P": 9, "M": 14, "G": 18},
    "AC": {"P": 11, "M": 16, "G": 20}
}


total_pedido = 0

while True:
   
    sabor = input("Digite o sabor (CP para Cupuaçu / AC para Açaí): ").strip().upper()
    if sabor not in ["CP", "AC"]:
        print("Sabor inválido. Tente novamente.")
        continue  
    
    
    tamanho = input("Digite o tamanho (P/M/G): ").strip().upper()
    if tamanho not in ["P", "M", "G"]:
        print("Tamanho inválido. Tente novamente.")
        continue 
    
    
    preco = precos[sabor][tamanho]
    total_pedido += preco  
    print(f"Pedido adicionado: {sabor} tamanho {tamanho} - R$ {preco}")
    
    
    mais_pedidos = input("Deseja pedir mais alguma coisa? (S/N): ").strip().upper()
    if mais_pedidos != "S":
        break 

print(f"Total do pedido: R$ {total_pedido}")
print("Obrigado por comprar conosco!")