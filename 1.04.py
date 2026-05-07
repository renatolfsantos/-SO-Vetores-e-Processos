def CalcTotal(n, total):
    return n + total

def VerAcima(n):
    if n > 6:
        return 1
    else:
        return 0
    
def VerPosAbaixo(n, pos):
    if n < 6:
        print(f'O aluno de posição {pos} está abaixo da média.')

def main():
    vet:list = [0] * 30
    somaTotal:int = 0
    acima:int = 0

    for i in range(30):
        vet[i] = int(input('Digite um valor: '))

        somaTotal = CalcTotal(vet[i], somaTotal)
        acima += VerAcima(vet[i])
        VerPosAbaixo(vet[i], i)

    print(f'A média do grupo é: {somaTotal / 30}')
    print(f'A quantidade de alunos acima da média é de: {acima}')


if __name__ == '__main__':
    main()