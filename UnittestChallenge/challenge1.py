import unittest
from typing import Any


def donuts(count: Any) -> str:
    """Dado um `count` como sendo o número de donuts,
    retorna uma string na forma "Número de donuts: `count`".
    Caso `count` seja maior ou igual a 10, retorna _many_.

    Args:
        count (int | str): A quantidade de donuts.

    Returns:
        str: A frase contendo o número de donuts.
    """
    if count >= 10:
        count = 'many'
    return f'Number of donuts: {count}'


def donutsV2(count: int) -> str:
    """Uma segunda versão da função `donuts`.

    Args:
        count (int): A quantidade de donuts.

    Returns:
        str: A frase contendo o número de donuts.
    """
    return 'many' if count >= 10 else f'Number of donuts: {count}'


def both_ends(s: str) -> str:
    """Dada uma string qualquer `s`, retorna uma string composta dos
    dois primeiros e os dois últimos caracteres, exemplo:

    - panela ----> pala
    - bala   ----> bala
    - mao    ----> maao
    - ja     ----> jaja

    Caso a string `s` contenha menos que 2 caracteres,
    retorna "" (string de comprimento 0).

    Args:
        s (str): A palavra a ser analisada.

    Returns:
        str: Os primeiros e últimos dois caracteres da string base.
    """
    if len(s) < 2:
        s = ''
    return f'{s[:2]}{s[-2:]}'


def fix_start(s: str) -> str:
    """Dada uma string `s`, retorna uma string onde todas as ocorrências de seu
    primeiro caractere sejam alteradas para "*", exceto o primeiro caractere.
    \nExemplo: babble ---> ba**le

    Args:
        s (str): A palavra a ser analisada.

    Returns:
        str: A string com os caracteres alterados.
    """
    return f'{s[0]}{s[1:].replace(s[0], "*")}' if len(s) > 0 and s.count(s[0]) > 1 else s


def mix_up(a: str, b: str) -> str:
    """Dadas duas strings `a` e `b`, troca os dois primeiros caracteres
    entre as variáveis e retorna uma única string separada por espaço.
    \nExemplo: "pezzy", "firm" ----> "fizzy perm"

    Args:
        a (str): A primeira palavra.
        b (str): A segunda palavra.

    Returns:
        str: A união invertida das duas palavras.
    """
    return f'{a.replace(a[0:2], b[0:2])} {b.replace(b[0:2], a[0:2])}'


class MyTest(unittest.TestCase):
    def test_donuts(self):
        self.assertEqual(donuts(4), 'Number of donuts: 4')
        self.assertEqual(donuts(9), 'Number of donuts: 9')
        self.assertEqual(donuts(10), 'Number of donuts: many')
        self.assertEqual(donuts(99), 'Number of donuts: many')

    def test_both_ends(self):
        self.assertEqual(both_ends('spring'), 'spng')
        self.assertEqual(both_ends('Hello'), 'Helo')
        self.assertEqual(both_ends('a'), '')
        self.assertEqual(both_ends('xyz'), 'xyyz')
        self.assertEqual(both_ends('xy'), 'xyxy')

    def test_fix_start(self):
        self.assertEqual(fix_start('babble'), 'ba**le')
        self.assertEqual(fix_start('aardvark'), 'a*rdv*rk')
        self.assertEqual(fix_start('google'), 'goo*le')
        self.assertEqual(fix_start('donut'), 'donut')

    def test_mix_up(self):
        self.assertEqual(mix_up('mix', 'pod'), 'pox mid')
        self.assertEqual(mix_up('dog', 'dinner'), 'dig donner')
        self.assertEqual(mix_up('gnash', 'sport'), 'spash gnort')
        self.assertEqual(mix_up('pezzy', 'firm'), 'fizzy perm')



if __name__ == '__main__':
    unittest.main()
