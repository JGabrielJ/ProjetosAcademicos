import unittest


def match_ends(words: list[str]) -> int:
    """Dada uma lista de strings `words`, retorna o total de strings se:
    1. cada palavra for maior ou igual a dois;
    2. o primeiro caractere coincidir com o último.

    Args:
        words (list[str]): A lista com as palavras a serem analisadas.

    Returns:
        int: O número total de palavras que satisfazem as condições.
    """
    count: int = 0
    for word in words:
        if len(word) >= 2 and word[0] == word[-1]:
            count += 1
    return count


def front_x(words: list[str]) -> list[str]:
    """Dada uma lista de strings, retorna uma lista de strings ordenadas,
    Entretanto, virá primeiro todo grupo de strings que comece com "x".

    Args:
        words (list[str]): A lista de palavras a serem analisadas.

    Returns:
        list[str]: A lista com as palavras ordenadas.
    """
    list_w, list_x = [], []
    for word in words:
        list_x.append(word) if word[0] == 'x' else list_w.append(word)
    list_x.sort(); list_w.sort()
    return list_x + list_w


def last(a: tuple[int]) -> int:
    """Retorna o último elemento de uma tupla.

    Args:
        a (tuple): A tupla com os elementos a serem organizados.

    Returns:
        int: O último elemento da tupla especificada.
    """
    return a[-1]

def sort_last(tuples: list[tuple]) -> list[tuple]:
    """Dada uma lista de tuplas não vazias, retorna uma
    lista ordenada pelo último elemento de cada tupla.

    Args:
        tuples (list[tuple]): A lista de tuplas a serem analisadas.

    Returns:
        list[tuple]: A lista com as tuplas ordenadas.
    """
    return sorted(tuples, key=last)


class MyTest(unittest.TestCase):
    def test_match_ends(self):
        self.assertEqual(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
        self.assertEqual(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
        self.assertEqual(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    def test_front_x(self):
        self.assertEqual(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']), ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
        self.assertEqual(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']), ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
        self.assertEqual(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']), ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

    def test_sort_last(self):
        self.assertEqual(sort_last([(1, 3), (3, 2), (2, 1)]), [(2, 1), (3, 2), (1, 3)])
        self.assertEqual(sort_last([(2, 3), (1, 2), (3, 1)]), [(3, 1), (1, 2), (2, 3)])
        self.assertEqual(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]), [(2, 2), (1, 3), (3, 4, 5), (1, 7)])



if __name__ == '__main__':
    unittest.main()
