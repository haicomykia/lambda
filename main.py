def append_title(title: str) -> None:
    """
    敬称をつけた名前のリストを出力
    :param title: 敬称
    :return: 敬称をつけた名前
    """
    names = ['鈴木', '佐藤', '田中']
    first_names = ['めい', 'ゆづき', 'ひなた']
    result = list(map(lambda x, y: x + y + title, names, first_names))
    print(result)


def filter_over_10() -> None:
    """
    10より大きい数を出力
    :return: 10より大きい数を出力
    """
    numbers = (5, 8, 10, 12, 30)
    result = list(filter(lambda x: x > 10, numbers))
    print(result)


def exists_any_over_10_numbers() -> bool:
    """
    10より大きい数字があるか返す
    :return: 10より大きい数字があるか?
    """
    numbers = (x for x in range(1, 11))
    return any(x > 10 for x in numbers)


def counts_over_10_numbers() -> int:
    """
    10より大きい数字の数を返す
    :return: 10より大きい数字の数
    """
    numbers = (x for x in range(1, 11))
    # 合計を求める
    # return sum([1, 2, 3, 4])
    # Falseは0, Trueは1とみなされるのでジェネレータ式と組み合わせて要素の数を変えられる
    return sum(x > 10 for x in numbers)


if __name__ == "__main__":
    append_title('様')
    filter_over_10()
    assert exists_any_over_10_numbers() == False
    assert counts_over_10_numbers() == 0
