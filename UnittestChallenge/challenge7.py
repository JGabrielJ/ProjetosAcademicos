from typing import Any


def sleep(week_day: bool, holiday: bool) -> bool:
    """Verifica se é dia de dormir.

    Args:
        week_day (bool): Um dia da semana.
        holiday (bool): Um feriado qualquer.

    Returns:
        bool: Pode dormir se for feriado ou não for dia da semana.
    """
    return True if holiday or not week_day else False


def stud_exp(a_smiling: bool, b_smiling: bool) -> bool:
    """Verifica se dois alunos estão com a mesma expressão.

    Args:
        a_smiling (bool): Expressão do aluno A.
        b_smiling (bool): Expressão do aluno B.
    
    Returns:
        bool: O resultado da comparação.
    """
    return True if (a_smiling and b_smiling) or (not a_smiling and not b_smiling) else False


def double_sum(a: int, b: int) -> int:
    """Soma dois números inteiros; se forem iguais, multiplica por dois.

    Args:
        a (int): Primeiro número.
        b (int): Segundo número.
    
    Returns:
        int: O resultado da operação.
    """
    return (a + b) * 2 if a == b else a + b


def absdiffv1(n: int) -> int:
    """Calcula a diferença absoluta entre um número `n` e 21.
    Caso `n` seja maior que 21, retorna o dobro da diferença absoluta.

    Args:
        n (int): O número a ser analisado.

    Returns:
        int: O resultado da operação.
    """
    return abs(n - 21) * 2 if n > 21 else abs(n - 21)


def parrot(speaking: bool, hour: int = 0) -> bool:
    """Verifica se um papagaio está falando entre 20h e 07h.

    Args:
        speaking (bool): Se Verdadeiro, o papagaio está gritando.
        hour (int): O horário atual em que o papagaio fala.
    
    Returns:
        bool: O veredito para a situação da ave.
    """
    return True if speaking and (hour < 7 or hour > 20) else False


def is_ten(a: int, b: int) -> bool:
    """Verifica se um dos números é 10 ou se sua soma é 10.

    Args:
        a (int): O primeiro número.
        b (int): O segundo número.
    
    Returns:
        bool: O resultado da comparação.
    """
    return True if a == 10 or b == 10 or a + b == 10 else False


def absdiffv2(n: int) -> bool:
    """Verifica se a diferença absoluta entre um
    número `n` e 100 ou 200 é menor ou igual a 10.

    Args:
        n (int): O número a ser analisado.

    Returns:
        bool: O resultado da operação.
    """
    return True if abs(n - 100) <= 10 or abs(n - 200) <= 10 else False


def delete(s: str, n: int) -> str:
    """Apaga uma letra na posição especificada.

    Args:
        s (str): A palavra que será analisada.
        n (int): A posição da letra a ser deletada.

    Returns:
        str: A string com uma letra a menos.
    """
    string = [l for l in s]
    string.pop(n); return ''.join(string)


def invert(s: str) -> str:
    """Inverte a primeira e última letra de uma string.

    Args:
        s (str): A string que será analisada.

    Returns:
        str: A palavra com as letras invertidas.
    """
    string = []

    if s != '':
        string = [l for l in s]
        string[0], string[-1] = string[-1], string[0]

    return ''.join(string) if len(s) > 1 else s


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
    print('\033[34mÉ dia de dormir?\033[1;m')
    test(sleep(False, False), True)
    test(sleep(True, False), False)
    test(sleep(False, True), True)
    test(sleep(True, True), True)

    print('\n\033[34mVai dar problema?\033[1;m')
    test(stud_exp(True, True), True)
    test(stud_exp(False, False), True)
    test(stud_exp(True, False), False)
    test(stud_exp(False, True), False)

    print('\n\033[34mSoma ou Dobro:\033[1;m')
    test(double_sum(1, 2), 3)
    test(double_sum(3, 2), 5)
    test(double_sum(2, 2), 8)
    test(double_sum(-1, 0), -1)
    test(double_sum(0, 0), 0)
    test(double_sum(0, 1), 1)

    print('\n\033[34mDiferença Absoluta (1):\033[1;m')
    test(absdiffv1(19), 2)
    test(absdiffv1(10), 11)
    test(absdiffv1(21), 0)
    test(absdiffv1(22), 2)
    test(absdiffv1(25), 8)
    test(absdiffv1(30), 18)

    print('\n\033[34mO papagaio está perturbando?\033[1;m')
    test(parrot(True, 6), True)
    test(parrot(True, 7), False)
    test(parrot(False, 6), False)
    test(parrot(True, 21), True)
    test(parrot(False, 21), False)
    test(parrot(True, 23), True)
    test(parrot(True, 20), False)

    print('\n\033[34mÉ dez?\033[1;m')
    test(is_ten(9, 10), True)
    test(is_ten(9, 9), False)
    test(is_ten(1, 9), True)
    test(is_ten(10, 1), True)
    test(is_ten(10, 10), True)
    test(is_ten(8, 2), True)
    test(is_ten(8, 3), False)
    test(is_ten(10, 42), True)
    test(is_ten(12, -2), True)

    print('\n\033[34mDiferença Absoluta (2):\033[1;m')
    test(absdiffv2(93), True)
    test(absdiffv2(90), True)
    test(absdiffv2(89), False)
    test(absdiffv2(110), True)
    test(absdiffv2(111), False)
    test(absdiffv2(121), False)
    test(absdiffv2(0), False)
    test(absdiffv2(5), False)
    test(absdiffv2(191), True)
    test(absdiffv2(189), False)
    test(absdiffv2(190), True)
    test(absdiffv2(200), True)
    test(absdiffv2(210), True)
    test(absdiffv2(211), False)
    test(absdiffv2(290), False)

    print('\n\033[34mDeletando letras:\033[1;m')
    test(delete('kitten', 1), 'ktten')
    test(delete('kitten', 0), 'itten')
    test(delete('kitten', 2), 'kiten')
    test(delete('kitten', 4), 'kittn')
    test(delete('Hi', 0), 'i')
    test(delete('Hi', 1), 'H')
    test(delete('code', 0), 'ode')
    test(delete('code', 1), 'cde')
    test(delete('code', 2), 'coe')
    test(delete('code', 3), 'cod')
    test(delete('chocolate', 8), 'chocolat')

    print('\n\033[34mInvertendo letras:\033[1;m')
    test(invert('code'), 'eodc')
    test(invert('a'), 'a')
    test(invert('ab'), 'ba')
    test(invert('abc'), 'cba')
    test(invert(''), '')
    test(invert('Chocolate'), 'ehocolatC')
    test(invert('nythoP'), 'Python')
    test(invert('hello'), 'oellh')



if __name__ == '__main__':
    main()
    print(f'\n\n\033[33m- {total} testes executados',
          f'\n- {success} funcionaram',
          f'\n- {total - success} falharam',
          f'\n- Média de acerto: {float(success * 10) / total:.1f}\033[1;m')
