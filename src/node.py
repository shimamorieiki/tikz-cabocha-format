"""_summary_
"""
from typing import List


class Node:
    """_summary_
    グラフに書くときの座標
    """

    def __init__(self, midashi: str, bnst_id: int, parent_id: int):
        self.midasai: str = midashi  # 見出し
        self.bnst_id: int = bnst_id  # 文節番号
        self.parent_id: int = parent_id  # 係り先文節番号
        self.depth: int = 0  # 係り受けの深さ
        self.start_x: float = 0  # 始点のx座標
        self.start_y: float = 0  # 始点のy座標
        self.end_x: float = 0  # 終点のx座標
        self.end_y: float = 0  # 終点のy座標

    def get_template(self) -> str:
        """_summary_
            1つのノードに相当する線分のテンプレート
        Returns:
            str: _description_
        """
        return f"\t\\draw[thick]  ({self.start_x},{self.start_y}) -| ({self.end_x},{self.end_y}) node [pos=0, anchor=east] {{{self.midasai}}};\n"

    def to_list(self) -> List[str | int | float]:
        """_summary_
            list
        Returns:
            _type_: _description_
        """
        return [
            self.midasai,
            self.bnst_id,
            self.parent_id,
            self.depth,
            self.start_x,
            self.start_y,
            self.end_x,
            self.end_y,
        ]

    def __str__(self) -> str:
        return ",".join([str(i) for i in self.to_list()])
