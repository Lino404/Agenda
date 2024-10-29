##sistema de cadastro
cadastros = []

##funçao para salvar os cadastros
def salvar_cadastro(login, senha):
    with open('senhas_logins.txt', 'a') as arquivo:
        arquivo.write(f"{login}:{senha}\n")

##funçao para ler os cadastros
def carregar_cadastros():
    try:
        with open('senhas_logins.txt', 'r') as arquivo:
            for linha in arquivo:
                login, senha = linha.strip().split(":")
                cadastros.append({"login": login, "senha": senha})
    except FileNotFoundError:
        pass

carregar_cadastros()

while True:
    print("\n╔════════ Cadastro e Login ════════╗")
    print("║      Realizar Cadastro(1):       ║")
    print('║        Efetuar login(2)          ║')
    print('╚══════════════════════════════════╝')  
    escolha = int(input("\nSelecione: "))

    if escolha == 1:
        loginC = input("\nCadastre seu Usuário: ")
        senhaC = input("Cadastre sua senha(Minimo 8 caracteres): ")

        while len(senhaC) < 8:
            senhaC = input("Digite uma senha com no minimo 8 caracteres: ")
        
        salvar_cadastro(loginC, senhaC)
        cadastros.append({'login': loginC, 'senha': senhaC})
        print("\n═══════════════════════════════════════════\n")
        print("   ✅ Cadastro realizado com sucesso!\n")
        print("═══════════════════════════════════════════\n")
        login_sucesso = True

    elif escolha == 2:
        login_sucesso = False
        while not login_sucesso:
            login_L = input("\nDigite seu Úsuario: ")
            senha_L = input("Digite sua Senha: ")

            for usuario in cadastros:
                if usuario["login"] == login_L and usuario["senha"] == senha_L:
                    print("\n═══════════════════════════════════════════\n")
                    print("    🎉 Login realizado com sucesso!\n")
                    print("═══════════════════════════════════════════\n")
                    login_sucesso = True
                    break
                
            if not login_sucesso:
                print("═══════════════════════════════════════════════\n")
                print("     ❌ Usuário ou Senha incorreto(s)\n")
                print("═══════════════════════════════════════════════\n")

    else:
        print("\nOpção Invalida")

    if login_sucesso:
        break

##sistema de atividades
cadastro_atividades = []

def menu():
    print("╔═════════════ MENU ═════════════╗")
    print("║  1. Cadastrar nova atividade   ║")
    print("║  2. Editar atividade           ║")
    print("║  3. Excluir atividade          ║")
    print("║  4. Visualizar atividades      ║")
    print("║  5. Sair                       ║")
    print("╚════════════════════════════════╝")
    return input("Escolha uma opção: ")

def salvar_atividades():
    # Salva as atividades no arquivo txt
    with open("atividades.txt", "w") as file:
        for atividade in cadastro_atividades:
            file.write(";".join(atividade) + "\n")

def carregar_atividades():
    try:
        with open('atividades.txt', 'r') as arquivo:
            for linha in arquivo:
                titulo, descricao, data_inicio, data_fim, prioridade = linha.strip().split(";")
                cadastro_atividades.append([titulo, descricao, data_inicio, data_fim, prioridade])
    except FileNotFoundError:
        pass

def cadastrar_atividade():
    titulo = input("Título da atividade: ")
    descricao = input("Descrição: ")
    data_inicio = input("Data de início: ")
    data_fim = input("Data de entrega: ")
    prioridade = input("Nível de prioridade (Baixa, Média, Alta): ")
    cadastro_atividades.append([titulo, descricao, data_inicio, data_fim, prioridade])
    salvar_atividades()
    print("Atividade cadastrada com sucesso!")

def editar_atividade():
    try:
        for i, atividade in enumerate(cadastro_atividades, 1):
            print(f"\nAtividade {i}:")
            print(f"  Título: {atividade[0]}")
            print(f"  Descrição: {atividade[1]}")
            print(f"  Data de Início: {atividade[2]}")
            print(f"  Data de Fim: {atividade[3]}")
            print(f"  Prioridade: {atividade[4]}")

        index = int(input("\nInforme o número da atividade que deseja editar: ")) - 1
        if 0 <= index < len(cadastro_atividades):
            titulo = input("Novo título da atividade: ")
            descricao = input("Nova descrição: ")
            data_inicio = input("Nova data de início: ")
            data_fim = input("Nova data de entrega: ")
            prioridade = input("Novo nível de prioridade (Baixa, Média, Alta): ")

            cadastro_atividades[index] = [titulo, descricao, data_inicio, data_fim, prioridade]
            salvar_atividades()
            print("Atividade editada com sucesso!")
    except (ValueError, IndexError):
        print("Erro ao editar atividade. Tente novamente.")

def excluir_atividade():
    try:
        for i, atividade in enumerate(cadastro_atividades, 1):
            print(f"\nAtividade {i}:")
            print(f"  Título: {atividade[0]}")
            print(f"  Descrição: {atividade[1]}")
            print(f"  Data de Início: {atividade[2]}")
            print(f"  Data de Fim: {atividade[3]}")
            print(f"  Prioridade: {atividade[4]}")

        index = int(input("\nInforme o número da atividade que deseja excluir: ")) - 1
        if 0 <= index < len(cadastro_atividades):
            del cadastro_atividades[index]
            salvar_atividades()
            print("Atividade excluída com sucesso!")
        else:
            print("Número de atividade inválido.")
    except (ValueError, IndexError):
        print("Erro ao excluir atividade. Tente novamente.")

def visualizar_atividades():
    if not cadastro_atividades:
        print("Nenhuma atividade cadastrada.")
        return

    print("\n--- ATIVIDADES CADASTRADAS ---")
    for i, atividade in enumerate(cadastro_atividades, 1):
        print(f"\nAtividade {i}:")
        print(f"  Título: {atividade[0]}")
        print(f"  Descrição: {atividade[1]}")
        print(f"  Data de Início: {atividade[2]}")
        print(f"  Data de Fim: {atividade[3]}")
        print(f"  Prioridade: {atividade[4]}")

carregar_atividades()  

while True:
    opcao = menu()
    if opcao == "1":
        cadastrar_atividade()
    elif opcao == "2":
        editar_atividade()
    elif opcao == "3":
        excluir_atividade()
    elif opcao == "4":
        visualizar_atividades()  
    elif opcao == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
