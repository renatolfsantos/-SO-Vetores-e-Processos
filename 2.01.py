import platform
import subprocess

def identificar_so():
    return platform.system()

def main():
    so:str = identificar_so()
    saida:str = ''
    linhas:list = []
    ultima_linha:str = ''
    partes:list = []
    media:float = 0.0

    if so == "Windows":
        comando = ["ping", "-4", "-n", "10", "www.google.com.br"]

    elif so == "Linux":
        comando = ["ping", "-4", "-c", "10", "www.google.com.br"]

    else:
        print("SO não suportado")
        return

    processo = subprocess.run(comando, capture_output=True, text=True)
    saida = processo.stdout

    linhas = saida.splitlines()

    if so == "Windows":
        ultima_linha = linhas[-1]

        partes = ultima_linha.split(",")

        media = partes[-1].split("=")[1].strip()
        print(f"Media do ping: {media}")

    else:
        ultima_linha = linhas[-1]

        partes = ultima_linha.split("=")

        valores = partes[1].strip().split("/")

        media = valores[1]
        print(f"Media do ping: {media} ms")


if __name__ == "__main__":
    main()