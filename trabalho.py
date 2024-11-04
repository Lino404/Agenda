import os
from colorama import Fore, Style, init
init()

color = {
    'green' : Fore.GREEN,
    'cyan' : Fore.CYAN,
    'red' : Fore.RED,
    'yellow' : Fore.YELLOW
}


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

login_sucesso = False

while login_sucesso == False:
    print(" ")
    print(f"{color['yellow']}╔════════ Cadastro e Login ════════╗{Style.RESET_ALL}")
    print(f"{color['yellow']}║                                  ║{Style.RESET_ALL}")
    print(f"{color['yellow']}║      Realizar Cadastro(1):       ║{Style.RESET_ALL}")
    print(f"{color['yellow']}║        Efetuar login(2)          ║{Style.RESET_ALL}")
    print(f"{color['yellow']}║                                  ║{Style.RESET_ALL}")
    print(f"{color['yellow']}╚══════════════════════════════════╝{Style.RESET_ALL}")
    escolha = input(f"\n{color['cyan']}Selecione: {Style.RESET_ALL}")

    if escolha == '1':
        print("\n═══════════════════════════════════════════════\n")
        loginC = input(f"{color['cyan']}Cadastre seu Usuário: {Style.RESET_ALL}\n")
        senhaC = input(f"{color['cyan']}Cadastre sua senha(Minimo 8 caracteres): {Style.RESET_ALL}\n")
        print("\n═══════════════════════════════════════════════\n")
        while len(senhaC) < 8:
            senhaC = input(f"{color['red']}Senha Curta! Digite uma senha com no minimo 8 caracteres: {Style.RESET_ALL}")
        
        salvar_cadastro(loginC, senhaC)
        cadastros.append({'login': loginC, 'senha': senhaC})
        os.system("cls")
        print("\n═══════════════════════════════════════════\n")
        print(f"{color['green']}   ✅ Cadastro realizado com sucesso!{Style.RESET_ALL}\n")
        print("═══════════════════════════════════════════\n")
        login_sucesso = True

    elif escolha == "2":
        login_sucesso = False
        while not login_sucesso:
            print("═══════════════════════════════════════════════")
            login_L = input(f"\n{color['cyan']}Digite seu Usuário: {Style.RESET_ALL}\n")
            senha_L = input(f"{color['cyan']}Digite sua Senha: {Style.RESET_ALL}\n")
            print("\n═══════════════════════════════════════════════\n")

            for usuario in cadastros:
                if usuario["login"] == login_L and usuario["senha"] == senha_L:
                    os.system("cls")
                    print("\n═══════════════════════════════════════════\n")
                    print(f"{color['green']}   🎉 Login realizado com sucesso!{Style.RESET_ALL}\n")
                    print("═══════════════════════════════════════════\n")
                    login_sucesso = True
                    break
                
            if not login_sucesso:
                os.system("cls")
                print("\n═══════════════════════════════════════════════\n")
                print(f"{color['red']}     ❌ Usuário ou Senha incorreto(s){Style.RESET_ALL}\n")
                print("═══════════════════════════════════════════════\n")
                break
    else:
        os.system("cls")
        print("\n═══════════════════════════════════════════════\n")
        print(f"{color['red']}Opção Invalida{Style.RESET_ALL}")
        print("\n═══════════════════════════════════════════════\n")

##sistema de atividades
cadastro_atividades = []

def menu():
    
    print(f"{color['yellow']}╔═════════════ MENU ═════════════╗{Style.RESET_ALL}")
    print(f"{color['yellow']}║                                ║{Style.RESET_ALL}")
    print(f"{color['yellow']}║  1. Cadastrar nova atividade   ║{Style.RESET_ALL}")
    print(f"{color['yellow']}║  2. Editar atividade           ║{Style.RESET_ALL}")
    print(f"{color['yellow']}║  3. Excluir atividade          ║{Style.RESET_ALL}")
    print(f"{color['yellow']}║  4. Visualizar atividades      ║{Style.RESET_ALL}")
    print(f"{color['yellow']}║  5. Sair                       ║{Style.RESET_ALL}")
    print(f"{color['yellow']}║                                ║{Style.RESET_ALL}")
    print(f"{color['yellow']}╚════════════════════════════════╝{Style.RESET_ALL}")
    return input(f"{color['cyan']}Escolha uma opção: {Style.RESET_ALL}")

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
    print("\n╔════════════════════════════════════════╗\n")
    titulo = input(f"{color['yellow']}Título da atividade: {Style.RESET_ALL}")
    descricao = input(f"{color['yellow']}Descrição: {Style.RESET_ALL}")
    data_inicio = input(f"{color['yellow']}Data de início: {Style.RESET_ALL}")
    data_fim = input(f"{color['yellow']}Data de entrega: {Style.RESET_ALL}")
    prioridade = input(f"{color['yellow']}Nível de prioridade (Baixa, Média, Alta): {Style.RESET_ALL}")
    cadastro_atividades.append([titulo, descricao, data_inicio, data_fim, prioridade])
    salvar_atividades()
    print(f"{color['green']}Atividade cadastrada com sucesso!{Style.RESET_ALL}\n")
    print("╚════════════════════════════════════════╝\n")

def editar_atividade():
    try:
        for i, atividade in enumerate(cadastro_atividades, 1):
            print(f"\n╔══════════ Atividade {i} ═══════════╗")
            print(f"  {color['yellow']}Título: {Style.RESET_ALL}{atividade[0]}")
            print(f"  {color['yellow']}Descrição: {Style.RESET_ALL}{atividade[1]}")
            print(f"  {color['yellow']}Data de Início: {Style.RESET_ALL}{atividade[2]}")
            print(f"  {color['yellow']}Data de Fim: {Style.RESET_ALL}{atividade[3]}")
            print(f"  {color['yellow']}Prioridade: {Style.RESET_ALL}{atividade[4]}")
            print(f"╚══════════════════════════════════╝\n")

        index = int(input("\nInforme o número da atividade que deseja editar: ")) - 1
        if 0 <= index < len(cadastro_atividades):
            titulo = input(f"{color['yellow']}Novo título da atividade: {Style.RESET_ALL}")
            descricao = input(f"{color['yellow']}Nova descrição: {Style.RESET_ALL}")
            data_inicio = input(f"{color['yellow']}Nova data de início: {Style.RESET_ALL}")
            data_fim = input(f"{color['yellow']}Nova data de entrega: {Style.RESET_ALL}")
            prioridade = input(f"{color['yellow']}Novo nível de prioridade (Baixa, Média, Alta): {Style.RESET_ALL}")

            cadastro_atividades[index] = [titulo, descricao, data_inicio, data_fim, prioridade]
            salvar_atividades()
            print(f"{color['green']}Atividade editada com sucesso!{Style.RESET_ALL}\n")
    except (ValueError, IndexError):
        print(f"{color['red']}Erro ao editar atividade. Tente novamente.{Style.RESET_ALL}\n")

def excluir_atividade():
    try:
        for i, atividade in enumerate(cadastro_atividades, 1):
            print(f"\n╔══════════ Atividade {i} ═══════════╗")
            print(f"  {color['yellow']}Título: {Style.RESET_ALL}{atividade[0]}")
            print(f"  {color['yellow']}Descrição: {Style.RESET_ALL}{atividade[1]}")
            print(f"  {color['yellow']}Data de Início: {Style.RESET_ALL}{atividade[2]}")
            print(f"  {color['yellow']}Data de Fim: {Style.RESET_ALL}{atividade[3]}")
            print(f"  {color['yellow']}Prioridade: {Style.RESET_ALL}{atividade[4]}")
            print(f"╚══════════════════════════════════╝\n")

        index = int(input("\nInforme o número da atividade que deseja excluir: ")) - 1
        if 0 <= index < len(cadastro_atividades):
            del cadastro_atividades[index]
            salvar_atividades()
            print(f"{color['green']}Atividade excluída com sucesso!{Style.RESET_ALL}\n")
        else:
            print(f"{color['red']}Número de atividade inválido.{Style.RESET_ALL}\n")
    except (ValueError, IndexError):
        print("Erro ao excluir atividade. Tente novamente.")

def visualizar_atividades():
    if not cadastro_atividades:
        print(f"{color['red']}Nenhuma atividade cadastrada.{Style.RESET_ALL}\n")
        return

    print("\n--- ATIVIDADES CADASTRADAS ---")
    for i, atividade in enumerate(cadastro_atividades, 1):
        print(f"\n╔══════════ Atividade {i} ═══════════╗")
        print(f"{color['yellow']}Título: {Style.RESET_ALL}{atividade[0]}")
        print(f"{color['yellow']}Descrição: {Style.RESET_ALL}{atividade[1]}")
        print(f"{color['yellow']}Data de Início: {Style.RESET_ALL}{atividade[2]}")
        print(f"{color['yellow']}Data de Fim: {Style.RESET_ALL}{atividade[3]}")
        print(f"{color['yellow']}Prioridade: {Style.RESET_ALL}{atividade[4]}")
        print(f"╚══════════════════════════════════╝\n")

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
        print(f"{color['red']}Opção inválida. Tente novamente.{Style.RESET_ALL}")
