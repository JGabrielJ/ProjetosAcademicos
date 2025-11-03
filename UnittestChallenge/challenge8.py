from typing import Any


def temp_avg(temperatures: list[int]) -> list[int]:
    """Recebe uma lista com as temperaturas médias de cada mês e
    devolve uma lista com os números correspondentes aos meses que
    possuem temperatura superior à média anual.

    Args:
        temperatures (list[int]): A lista com as temperaturas médias de cada mês.

    Returns:
        list[int]: A lista de meses com a temperatura superior à média anual.
    """
    average = sum(temperatures) / len(temperatures)
    return [month for month in range(0, len(temperatures)) if temperatures[month] > average]


def over_13(ages: list[int], heights: list[float]) -> list[float]:
    """Recebe as idades e alturas de diferentes pessoas e filtra as
    alturas inferiores à média e das pessoas com mais de 13 anos.

    Args:
        ages (list[int]): A lista com as idades das pessoas.
        heights (list[float]): A lista com as alturas das pessoas.

    Returns:
        list[float]: A lista com as alturas abaixo da média.
    """
    average = sum(heights) / len(heights)
    return [heights[i] for i in range(0, len(heights)) if ages[i] > 13 and heights[i] < average]


def jump_avg(notes: list[float]) -> float:
    """Recebe uma lista com as notas dos saltos de um atleta e calcula a média
    dos saltos, assumindo que o melhor e o pior saltos serão desconsiderados.

    Args:
        notes (list[float]): A lista com as notas do atleta.

    Returns:
        float: A média dos saltos do atleta.
    """
    notes.remove(max(notes))
    notes.remove(min(notes))
    return sum(notes) / len(notes)


def prime_nums(start: int, end: int) -> list[int]:
    """Retorna uma lista de números primos que estão dentro do
    intervalo dos valores informados, incluindo os limites.

    Args:
        start (int): O limite inferior do intervalo.
        end (int): O limite superior do intervalo.

    Returns:
        list[int]: A lista com os números primos.
    """
    count: int = 0; primes: list = []
    for n in range(start, end + 1):
        for div in range(1, n + 1):
            if n % div == 0:
                count += 1
        if count == 2:
            primes.append(n)
        count = 0
    return primes


def fibonacci(n: int) -> list[int]:
    """Retorna uma lista com os `n` primeiros
    valores da sequência de Fibonacci.

    Args:
        n (int): O número que limita até onde vai a sequência.

    Returns:
        list[int]: A lista contendo os números de Fibonacci.
    """
    f: int = 1; fibo: list = []
    for _ in range(1, n + 1):
        fibo.append(f)
        if len(fibo) >= 2:
            f = fibo[-1] + fibo[-2]
    return fibo


def change_wage(wages: list[float]) -> list[float]:
    """Calcula o aumento de salário de acordo com a seguinte tabela:
    1. até 1 salário mínimo (inclusivo) → aumento de 20%;
    2. entre 1 e 2 salários mínimos (inclusivo) → aumento de 15%;
    3. entre 2 e 5 salários mínimos (inclusivo) → aumento de 10%;
    4. acima de 5 salários mínimos → aumento de 5%.

    Args:
        wages (list[float]): A lista com os salários inalterados.

    Returns:
        list[float]: A lista com os salários aumentados.
    """
    new_wages: list = []
    for w in wages:
        if w <= 724.00:         # Condição 1
            w += w * 20 / 100
        elif w <= 724.00 * 2:   # Condição 2
            w += w * 15 / 100
        elif w <= 724.00 * 5:   # Condição 3
            w += w * 10 / 100
        else:                   # Condição 4
            w += w * 5 / 100
        new_wages.append(w)
    return new_wages


success, total = 0, 0

def test(obtained: Any, expected: Any) -> None:
    """Testa diferentes valores baseado na função elaborada.

    Args:
        obtained (Any): O valor obtido pela função.
        expected (Any): O valor a ser retornado pela função.
    """
    global success, total; total += 1

    if obtained != expected:
        prefix = f'\033[31m{"Falhou"}'
    else:
        prefix = f'\033[32m{"Passou"}'; success += 1

    print(f'{prefix} -> Esperado: {repr(expected)} \tObtido: {repr(obtained)}\033[1;m')


def main():
    print('\033[34mMeses com a Temperatura acima da Média:\033[1;m')
    test(temp_avg([20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]), [])
    test(temp_avg([25, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]), [0])
    test(temp_avg([23, 25, 26, 24, 21, 22, 26, 24, 25, 22, 23, 19]), [1, 2, 3, 6, 7, 8])
    test(temp_avg([19, 20, 21, 20, 17, 18, 19, 20, 22, 21, 20]), [1, 2, 3, 7, 8, 9, 10])
    test(temp_avg([21, 22, 23, 21, 22, 22, 23, 21, 23, 22, 21, 23, 21]), [1, 2, 4, 5, 6, 8, 9, 11])

    print('\n\033[34mAlturas abaixo da Média:\033[1;m')
    test(over_13([13, 13, 14], [1.7, 1.7, 1.5]), [1.5])
    test(over_13([13, 13, 14, 13], [1.7, 1.7, 1.5, 1.6]), [1.5])
    test(over_13([14, 20], [1.6, 2]), [1.6])
    test(over_13([10, 7, 13, 15, 20, 21],[1.7, 1.21, 1.65, 2, 1.9, 1.5]), [1.5])
    test(over_13([14, 15, 16, 17, 18, 30], [1.9, 1.89, 1.85, 1.95, 2, 1.99]), [1.9, 1.89, 1.85])
    test(over_13([10, 9, 90, 9, 13, 14, 15], [1.25, 1.3, 1.7, 1.41, 1.5, 1.55, 1.7]), [])

    print('\n\033[34mMédia das Notas dos Saltos:\033[1;m')
    test(jump_avg([10, 10, 10, 10, 10]), 10)
    test(jump_avg([9, 9.1, 8, 7, 6.9]), 8)
    test(jump_avg([1, 1, 3, 5, 5]), 3)
    test(jump_avg([10, 10, 9.9, 10, 10]), 10)

    print('\n\033[34mLista de Números Primos:\033[1;m')
    test(prime_nums(0, 1), [])
    test(prime_nums(5, 10), [5, 7])
    test(prime_nums(10, 20), [11, 13, 17, 19])
    test(prime_nums(0, 21), [2, 3, 5, 7, 11, 13, 17, 19])
    test(prime_nums(43, 102), [43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101])

    print('\n\033[34mSequência de Fibonacci:\033[1;m')
    test(fibonacci(1), [1])
    test(fibonacci(2), [1, 1])
    test(fibonacci(3), [1, 1, 2])
    test(fibonacci(4), [1, 1, 2, 3])

    print('\n\033[34mAumentando Salários:\033[1;m')
    test(change_wage([500, 724.0, 725.00, 1448.00, 1449.00, 3620.00, 3621.00, 4000.00]),
        [600.0, 868.8, 833.75, 1665.2, 1593.9, 3982.0, 3802.05, 4200.0])



if __name__ == '__main__':
    main()
    print(f'\n\n\033[33m- {total} testes executados',
          f'\n- {success} funcionaram',
          f'\n- {total - success} falharam',
          f'\n- Média de acerto: {float(success * 10) / total:.1f}\033[1;m')
