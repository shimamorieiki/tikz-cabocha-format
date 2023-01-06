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

    # ノード間の高さのデフォルト値
    line_height_options: dict[str, float] = {
        "-xlarge": 1.0,
        "-large": 0.8,
        "-middle": 0.6,
        "-small": 0.4,
    }

    # ノード間の高さのデフォルト値(xlarge相当)
    default_line_heigth: float = 1.0

    # コマンドライン引数からcsvのファイルを受け取る
    data: List[Tuple[str, int, int]] = get_data(file_path=sys.argv[1])

    # グラフの高さを指定する
    line_height: float = default_line_heigth
    for key, value in line_height_options.items():
        if key in sys.argv:
            line_height = value

    # cabocha-formatのtikzコードを出力する
    Graph(data=data, line_height=line_height).print_tikz()


if __name__ == "__main__":
    main()
