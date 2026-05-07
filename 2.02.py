import platform
import subprocess

def identificar_os():
    return platform.system()

def executar_processo(so, opcao, parametro=None):

    comando = []

    if opcao == 1:
        if so == "Windows":
            comando = ["TASKLIST", "/FO", "TABLE"]

        elif so == "Linux":
            comando = ["ps", "-ef"]

    elif opcao == 2:
        if so == "Windows":
            comando = ["TASKKILL", "/PID", parametro]

        elif so == "Linux":
            comando = ["kill", "-9", parametro]

    elif opcao == 3:
        if so == "Windows":
            comando = ["TASKKILL", "/IM", parametro]

        elif so == "Linux":
            comando = ["pkill", "-f", parametro]

    processo = subprocess.run(comando, capture_output=True, text=True)

    print(processo.stdout)

    if processo.stderr:
        print("Erro:", processo.stderr)

def main():
    so = identificar_os()

    while True:
        print("\n1 - Listar processos")
        print("2 - Matar processo por PID")
        print("3 - Matar processo por Nome")
        print("9 - Encerrar")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            executar_processo(so, 1)

        elif opcao == 2:
            pid = input("Digite o PID: ")

            executar_processo(so, 2, pid)

        elif opcao == 3:
            nome = input("Digite o nome do processo: ")

            executar_processo(so, 3, nome)

        elif opcao == 9:
            print("Encerrando aplicação...")
            exit()

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()