def VerIntervalo(n):
    if 10 <= n <= 200:
        return n, 1
    return 0, 0

def VerImpares(n):
    if n % 2 != 0:
        return n
    return 0

def main():
    vet:list = [0] * 50
    somaTotal:int = 0
    vezes:int = 0
    somaImpares:int = 0

    for i in range(50):
        vet[i] = int(input("Digite um valor: "))
        valor, count = VerIntervalo(vet[i])
        somaTotal += valor
        vezes += count

        somaImpares += VerImpares(vet[i])

    if vezes > 0:
        print(f'A média dos valores entre 10 e 200 é: {somaTotal/vezes}')
    else:
        print("Nenhum valor no intervalo.")

    print(f'A soma dos números ímpares é: {somaImpares}')


if __name__ == '__main__':
    main()