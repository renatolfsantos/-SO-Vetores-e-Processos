def VerMaior(n, m):
    if n > m:
        return n
    else:
        return m
    
def VerMenor(n, m):
    if n < m:
        return n
    else:
        return m

def CalcTotal(n, total):
    return total + n

def main():
    vet:list = [0] * 100
    total:int = 0

    for i in range(100):
        vet[i] = int(input('Digite um valor: '))

    menor:int = vet[0]
    maior:int = vet[0]

    for i in range(100):
        maior = VerMaior(vet[i], maior)
        menor = VerMenor(vet[i], menor)

        total = CalcTotal(vet[i], total)

    print(f'O maior valor é: {maior}; O menor valor é: {menor}')
    print(f'A média dos valores é: {total/100}')

if __name__ == '__main__':
    main()