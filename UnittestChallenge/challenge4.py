import unittest


def remove_adjacent(nums: list[int]) -> list[int]:
    """Dada uma lista de números, retorna uma lista onde todo elemento
    adjacente e repetido será deletado e reduzido a um único elemento.
    \nExemplo: [1, 2, 2, 3] retornará [1, 2, 3].

    Args:
        nums (list[int]): A lista com os números a serem analisados.

    Returns:
        list[int]: A lista com os números simplificados.
    """
    numbers = nums.copy()
    for i in range(0, len(nums)):
        if i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                numbers.remove(nums[i])
    return numbers


def linear_merge(list1: list[str], list2: list[str]) -> list[str]:
    """Dadas duas listas ordenadas em ordem crescente, cria e retorna
    uma lista com todos os elementos em ordem alfabética.

    Args:
        list1 (list[str]): A primeira lista a ser analisada.
        list2 (list[str]): A segunda lista a ser analisada.

    Returns:
        list[str]: A lista com os elementos organizados em ordem alfabética.
    """
    list_final = list1 + list2
    list_final.sort(); return list_final


class MyTest(unittest.TestCase):
    def test_remove_adjacent(self):
        self.assertEqual(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
        self.assertEqual(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
        self.assertEqual(remove_adjacent([1, 2, 3, 2, 3]), [1, 2, 3, 2, 3])
        self.assertEqual(remove_adjacent([]), [])

    def test_linear_merge(self):
        self.assertEqual(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']), ['aa', 'bb', 'cc', 'xx', 'zz'])
        self.assertEqual(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']), ['aa', 'bb', 'cc', 'xx', 'zz'])
        self.assertEqual(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']), ['aa', 'aa', 'aa', 'bb', 'bb'])



if __name__ == '__main__':
    unittest.main()
