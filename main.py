"""_summary_
"""
import csv
import sys
from typing import List, Tuple

from src.graph import Graph


def get_data(file_path: str) -> List[Tuple[str, int, int]]:
    """_summary_
        csvを読み取りデータを取得する
    Args:
        file_path (_type_): _description_
    """
    with open(file=file_path, mode="r", encoding="utf-8") as read_file:
        reader = csv.reader(read_file)
        input_data = [(row[0], int(row[1]), int(row[2])) for row in reader]

    return input_data


def main() -> None:
    """_summary_"""

    # コマンドライン引数からcsvのファイルを受け取る
    data: List[Tuple[str, int, int]] = get_data(file_path=sys.argv[1])

    # cabocha-formatのtikzコードを出力する
    Graph(data=data).print_tikz()


if __name__ == "__main__":
    main()
