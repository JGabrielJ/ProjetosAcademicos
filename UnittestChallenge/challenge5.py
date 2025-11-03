from typing import Any


def buy_fruits(strawberry: float = 0, grape: float = 0) -> float:
    """Uma fruteira está vendendo frutas com a seguinte tabela de preços:
    | Produto / Preço |  Até 5 kg   | Acima de 5 kg |
    |-----------------|-------------|---------------|
    |     Morango     | R$2.50 / kg |  R$2.20 / kg  |
    |       Uva       | R$1.80 / kg |  R$1.50 / kg  |

    Se o cliente comprar mais de 8 kg em frutas ou o valor total da compra
    ultrapassar R$25.00, ele terá de receber um desconto de 10% sobre o total.

    Args:
        strawberry (float, optional): Quantidade de morangos. Defaults to 0.
        grape (float, optional): Quantidade de uvas. Defaults to 0.

    Returns:
        float: Valor total da compra (com ou sem desconto).
    """
    berry_price = 2.50 if strawberry <= 5 else 2.20
    grape_price = 1.80 if grape <= 5 else 1.50
    total_val = strawberry * berry_price + grape * grape_price

    if strawberry + grape > 8 or total_val > 25.00:
        total_val -= total_val * 10 / 100

    return round(total_val, 2)


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
    print('\033[34mComprando frutas:\033[1;m')

    # Testes de zeros
    test(buy_fruits(), 0.0)
    test(buy_fruits(strawberry=0), 0.0)
    test(buy_fruits(grape=0), 0.0)
    test(buy_fruits(strawberry=0, grape=0), 0.0)
    test(buy_fruits(grape=0, strawberry=0), 0.0)
    test(buy_fruits(strawberry=0), 0.0)


    # Testes apenas com morangos
    test(buy_fruits(strawberry=1, grape=0), 2.50)
    test(buy_fruits(strawberry=2, grape=0), 5.00)
    test(buy_fruits(strawberry=4, grape=0), 10.00)
    test(buy_fruits(strawberry=5, grape=0), 12.50)

    # Testes apenas com morangos, mudando a faixa
    test(buy_fruits(strawberry=6, grape=0), 13.20)
    test(buy_fruits(strawberry=5.1, grape=0), 11.22)
    test(buy_fruits(strawberry=8, grape=0), 17.60)

    # Testes apenas com morangos, recebendo desconto por peso
    test(buy_fruits(strawberry=9, grape=0), 17.82)
    test(buy_fruits(strawberry=10, grape=0), 19.80)

    # Testes apenas com morangos, recebendo desconto por preço
    test(buy_fruits(strawberry=20, grape=0), 39.60)


    # Testes apenas com uvas
    test(buy_fruits(strawberry=0, grape=1), 1.80)
    test(buy_fruits(strawberry=0, grape=2), 3.60)
    test(buy_fruits(strawberry=0, grape=4), 7.20)
    test(buy_fruits(strawberry=0, grape=5), 9.0)

    # Testes apenas com uvas, mudando a faixa
    test(buy_fruits(strawberry=0, grape=6), 9.00)
    test(buy_fruits(strawberry=0, grape=5.1), 7.65)
    test(buy_fruits(strawberry=0, grape=8), 12.00)

    # Testes apenas com uvas, recebendo desconto por peso
    test(buy_fruits(strawberry=0, grape=9), 12.15)
    test(buy_fruits(strawberry=0, grape=10), 13.5)

    # Testes apenas com uvas, recebendo desconto por preço
    test(buy_fruits(strawberry=0, grape=20), 27.00)


    # Testes com as duas frutas
    test(buy_fruits(strawberry=2, grape=2), 8.60)
    test(buy_fruits(strawberry=4, grape=4), 17.20)
    test(buy_fruits(strawberry=5, grape=5), 19.35)
    test(buy_fruits(strawberry=10, grape=10), 33.30)



if __name__ == '__main__':
    main()
    print(f'\n\n\033[33m- {total} testes executados',
          f'\n- {success} funcionaram',
          f'\n- {total - success} falharam',
          f'\n- Média de acerto: {float(success * 10) / total:.1f}\033[1;m')
