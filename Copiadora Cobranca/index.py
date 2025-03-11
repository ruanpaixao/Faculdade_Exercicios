print("Bem-vindo ao sistema de cobrança da copiadora! Desenvolvido por Ruan Paixão")
print ("Legenda da escolha: DIG - DIGITALIZAÇAO - ICO - IMPRESSÃO COLORIDA - IPB - IMPRESSÃO PRETO E BRANCO - FOT - FOTOCÓPIA ")

servicos = {
    "DIG": 1.10,  
    "ICO": 1.00,  
    "IPB": 0.40,  
    "FOT": 0.20   
}

def escolha_servico():
    """Pergunta o serviço desejado e retorna o valor correspondente."""
    while True:
        servico = input("Escolha o serviço (DIG, ICO, IPB, FOT): ").strip().upper()
        if servico in servicos:
            return servicos[servico]
        print("Serviço inválido. Tente novamente.")

def num_pagina():
    """Pergunta o número de páginas e aplica o desconto adequado."""
    while True:
        try:
            paginas = int(input("Digite o número de páginas: "))
            if paginas >= 20000:
                print("Quantidade de páginas não permitida. Tente novamente.")
                continue
            
            
            if paginas >= 2000:
                paginas *= 0.75  
            elif paginas >= 200:
                paginas *= 0.80  
            elif paginas >= 20:
                paginas *= 0.85  
            
            return paginas
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")

def servico_extra():
    """Pergunta o serviço extra desejado e retorna o valor correspondente."""
    extras = {"1": 15, "2": 40, "0": 0}
    while True:
        opcao = input("Deseja encadernação? (1-Simples - R$15, 2-Capa Dura - R$40, 0-Não): ").strip()
        if opcao in extras:
            return extras[opcao]
        print("Opção inválida. Tente novamente.")


valor_servico = escolha_servico()
n_pags = num_pagina()
extra = servico_extra()

total = (valor_servico * n_pags) + extra

print(f"Total a pagar: R$ {total:.2f}")
print("Obrigado por utilizar nossos serviços!")
