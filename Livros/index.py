print("Bem-vindo ao sistema de gerenciamento de livros! Desenvolvido por Ruan Paixão")

lista_livro = []

id_global = 0

def cadastrar_livro(id):
    """Cadastra um novo livro na lista."""
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o autor do livro: ")
    editora = input("Digite a editora do livro: ")
    
    livro = {"ID": id, "Nome": nome, "Autor": autor, "Editora": editora}
    lista_livro.append(livro)
    print("Livro cadastrado com sucesso!")

def consultar_livro():
    """Consulta livros com base na opção escolhida pelo usuário."""
    while True:
        print("\nOpções de consulta:")
        print("1 - Consultar Todos")
        print("2 - Consultar por ID")
        print("3 - Consultar por Autor")
        print("4 - Retornar ao menu")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            for livro in lista_livro:
                print(livro)
        elif opcao == "2":
            try:
                id_consulta = int(input("Digite o ID do livro: "))
                encontrado = False
                for livro in lista_livro:
                    if livro["ID"] == id_consulta:
                        print(livro)
                        encontrado = True
                        break
                if not encontrado:
                    print("ID não encontrado.")
            except ValueError:
                print("ID inválido. Digite um número inteiro.")
        elif opcao == "3":
            autor_consulta = input("Digite o nome do autor: ")
            encontrados = [livro for livro in lista_livro if livro["Autor"] == autor_consulta]
            if encontrados:
                for livro in encontrados:
                    print(livro)
            else:
                print("Nenhum livro encontrado para este autor.")
        elif opcao == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")

def remover_livro():
    """Remove um livro da lista com base no ID."""
    while True:
        try:
            id_remover = int(input("Digite o ID do livro a ser removido: "))
            for livro in lista_livro:
                if livro["ID"] == id_remover:
                    lista_livro.remove(livro)
                    print("Livro removido com sucesso!")
                    return
            print("ID inválido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

# Menu principal
while True:
    print("\nMenu Principal:")
    print("1 - Cadastrar Livro")
    print("2 - Consultar Livro")
    print("3 - Remover Livro")
    print("4 - Encerrar Programa")
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        id_global += 1
        cadastrar_livro(id_global)
    elif opcao == "2":
        consultar_livro()
    elif opcao == "3":
        remover_livro()
    elif opcao == "4":
        print("Encerrando o programa. Obrigado por utilizar o sistema!")
        break
    else:
        print("Opção inválida. Tente novamente.")
