import os
from typing import Any


def palindrome(text: str) -> bool:
    """Verifica se um determinado texto é um palíndromo.

    Args:
        text (str): Texto a ser verificado.

    Returns:
        bool: Verdadeiro se for um palíndromo, Falso caso não seja.
    """

    fixed_text = text.lower().replace(' ', ''); pal = fixed_text[::-1]
    if not fixed_text[-1].isalpha():
        fixed_text = fixed_text.replace(fixed_text[-1], ''); pal = pal.replace(pal[0], '')
    return pal == fixed_text


def change_case(text: str) -> str:
    """Alterna as caixas das letras entre alta e baixa, ou seja,
    vogais se tornam maiúsculas e consoantes ficam minúsculas.

    Args:
        text (str): Texto a ser alterado.

    Returns:
        str: Texto com as letras modificadas.
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    fixed_text = text.strip().lower()

    word = [let for let in fixed_text]
    for w in word:
        i = word.index(w)
        if w in vowels:
            word[i] = w.upper()

    fixed_text = ''.join(word)
    return fixed_text


def months_in_full(date: str) -> str:
    """Solicita a data de nascimento (dd/mm/aaaa) do usuário
    e a imprime com o nome do mês ao invés do número.

    Args:
        date (str): Data de nascimento do usuário.

    Returns:
        str: Data de nascimento reformatada com o mês por extenso.
    """
    fmt_date = date.split('/')
    month_list = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
                  'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    month = month_list[int(fmt_date[1]) - 1]
    return f'{fmt_date[0]} de {month} de {fmt_date[2]}'


def find_character(text: str, char: str) -> int | None:
    """Recebe um texto e retorna a localização da
    primeira vez que o caracter especificado aparece.

    Args:
        text (str): Texto a ser verificado.
        char (str): Caracter a ser procurado.

    Returns:
        int|None: Posição do caracter no texto, se houver.
    """
    try:
        return text.index(char)
    except ValueError:
        return None


def lucky_numbers(lower: int = 1, upper: int = 100000) -> int:
    """Informa quantos números contém o dígito 2 mas não o 7,
    dentro de um intervalo especificado (incluindo os extremos).

    Args:
        lower (int, optional): O limite inferior do intervalo. Defaults to 1.
        upper (int, optional): O limite superior do intervalo. Defaults to 100000.

    Returns:
        int: A quantidade de números "sortudos" dentro do intervalo dado.
    """
    count: int = 0
    for n in range(lower, upper + 1):
        num = str(n)
        if '2' in num and '7' not in num:
            count += 1
    return count


def phone_check(phones: list) -> int:
    """Para cada telefone, as seguintes regras devem ser cumpridas:
    1. Todos os telefones devem ter 6 dígitos apenas;
    2. Não pode haver dois dígitos consecutivos idênticos;
    3. A soma dos dígitos obrigatoriamente deve ser par;
    4. O último dígito não pode ser igual ao primeiro.

    Args:
        phones (list): Lista de telefones a serem analisados.

    Returns:
        int: A quantidade de números que cumprem os requisitos.
    """
    count: int = 0
    for ph in phones:
        cond: bool = True
        tel = [int(dig) for dig in ph]

        # Condição 1
        if len(tel) > 6:
            cond = False

        # Condição 2
        if cond:
            for i in range(0, len(tel)):
                if i < len(tel) - 1:
                    if tel[i] == tel[i + 1]:
                        cond = False

        # Condição 3
        if cond and sum(tel) % 2 != 0:
            cond = False

        # Condição 4
        if cond and tel[-1] != tel[0]:
            count += 1

    return count


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
    print('\033[34mPalíndromos:\033[1;m')
    test(palindrome('ovo'), True)
    test(palindrome('Ovo'), True)
    test(palindrome('Ovo '), True)
    test(palindrome(' Ovo '), True)
    test(palindrome('Assam a massa'), True)
    test(palindrome('Ame o poema!'), True)


    print('\n\033[34mMaíusculas / Minúsculas:\033[1;m')
    test(change_case('Araquari'), 'ArAqUArI')
    test(change_case('Caxias do Sul'), 'cAxIAs dO sUl')


    print('\n\033[34mMês por Extenso:\033[1;m')
    test(months_in_full('19/05/2014'), '19 de maio de 2014')
    test(months_in_full('25/12/2016'), '25 de dezembro de 2016')


    print('\n\033[34mEncontra Caracteres:\033[1;m')
    test(find_character('--*--', '*'), 2)
    test(find_character('19/05/2014', '/'), 2)
    test(find_character('19/05/2014', '.'), None)


    print('\n\033[34mNúmeros Sortudos:\033[1;m')
    test(lucky_numbers(18644, 33087), 7995)


    print('\n\033[34mVerificação de Telefones:\033[1;m')
    phone_list_lst = ['91775523', '88032828']
    test(phone_check(phone_list_lst), 0)

    phone_list_str = '''
        213752 216732 221063 221545 225583 229133 230648 233222
        236043 237330 239636 240138 242123 246224 249183 252936
        254711 257200 257607 261424 263814 266794 268649 273050
        275001 277606 278997 283331 287104 287953 289137 291591
        292559 292946 295180 295566 297529 300400 304707 306931
        310638 313595 318449 319021 322082 323796 326266 326880
        327249 329914 334392 334575 336723 336734 338808 343269
        346040 350113 353631 357154 361633 361891 364889 365746
        365749 366426 369156 369444 369689 372896 374983 375223
        379163 380712 385640 386777 388599 389450 390178 392943
        394742 395921 398644 398832 401149 402219 405364 408088
        412901 417683 440052 444630 463328 466458 486195 488359
        500877 502386 521455 524277 536593 537360 556493 558807
        579937 580112 590483 593112 601523 605761 618314 622752
        637656 641136 662224 666265 422267 447852 469601 489209
        502715 528496 539055 559102 580680 593894 608618 626345
        644176 668010 424767 449116 473108 489388 507617 529345
        540582 562050 582458 594293 609198 626632 644973 672480
        426613 453865 476773 491928 512526 531231 543708 564962
        583012 597525 610141 628889 647617 672695 430474 457631
        477956 496569 512827 531766 547492 569677 585395 598184
        610536 629457 652218 676868 433910 461750 481991 496964
        513796 535067 550779 570945 586244 600455 612636 629643
        657143 677125 435054 462985 482422 497901 518232 535183
        551595 575447 587393 600953 615233 633673 659902 678315
    '''.strip().split(); test(phone_check(phone_list_str), 39)

    phone_list_file = os.path.join(os.path.dirname(__file__), 'phone_list.txt')
    phone_list_txt = open(phone_list_file).read().strip().split(); test(phone_check(phone_list_txt), 39)



if __name__ == '__main__':
    main()
    print(f'\n\n\033[33m- {total} testes executados',
          f'\n- {success} funcionaram',
          f'\n- {total - success} falharam',
          f'\n- Média de acerto: {float(success * 10) / total:.1f}\033[1;m')
