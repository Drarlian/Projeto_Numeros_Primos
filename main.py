"""
Parâmetro: 2 milhões

Tempo de execução com o parâmetro: +/- 00:56:447  # -> 56 Minutos
"""
from multiprocessing import Pool
from time import time

def descobre_primo(numero_inicio, numero_final):
    if numero_final % 2 == 0 and numero_final != 2:
        numero_final -= 1
        mudou = True
    else:
        mudou = False

    lista_primos = []
    comeco = numero_inicio
    cont = 2

    while True:
        for c in range(2, numero_inicio):
            if numero_inicio % c == 0:
                cont = cont + 1

            if cont > 2 or c > (numero_inicio / 2):
                break

        if cont == 2:
            lista_primos.append(numero_inicio)

        if numero_inicio == numero_final:
            break
        else:
            if numero_inicio % 2 == 0:
                numero_inicio = numero_inicio + 1
                cont = 2
            else:
                numero_inicio = numero_inicio + 2
                cont = 2

    if mudou:
        numero_final += 1

    print(f'Lista dos números primos entre {comeco} e {numero_final} é: {lista_primos}')
    print(f'Tamanho da lista: {len(lista_primos)}')
    print(f'A soma dos números primos entre {comeco} e {numero_final} é de: {sum(lista_primos)}')
    print('-' * 60)
    return lista_primos


if __name__ == '__main__':
    pool = Pool(processes=4)

    inicio = time()

    c1 = 500_000
    c2 = 1_000_000
    c3 = 1_500_000
    c4 = 2_000_000

    r1 = pool.apply_async(descobre_primo, [2, c1])
    r2 = pool.apply_async(descobre_primo, [c1+1, c2])
    r3 = pool.apply_async(descobre_primo, [c2+1, c3])
    r4 = pool.apply_async(descobre_primo, [c3+1, c4])

    pool.close()
    pool.join()

    fim = time()

    print(f'Tempo de execução em segundos: {fim - inicio:.2f}s')
