"""_summary_
"""
from typing import List, Tuple

from .node import Node


class Graph:
    """_summary_"""

    def __init__(self, data: List[Tuple[str, int, int]], line_height: float) -> None:
        self.nodes: List[Node] = self.init_nodes(data=data)
        self.line_height = line_height

    def init_nodes(self, data: List[Tuple[str, int, int]]) -> List[Node]:
        """_summary_
            グラフのnodeのリストを取得する
        Args:
            data (List[Tuple[str, int, int]]): _description_
        """
        return [
            Node(midashi=midashi, bnst_id=bnst_id, parent_id=parent_id)
            for midashi, bnst_id, parent_id in data
        ]

    def get_nest_depth(self) -> None:
        """_summary_
            ネストの深さを取得する
        Args:
            data (List[Tuple[str, int, int]]): _description_
        """
        # 現在の入れ子の深さ
        for node in reversed(self.nodes):
            if node.parent_id == -1:
                # 係り先が -1 すなわち最後の文節のときは深さ0
                node.depth = 0
            else:
                # 係り先が -1 じゃないときは自分の係り先の深さ + 1
                node.depth = self.nodes[node.parent_id].depth + 1

        # いくつずらすか
        # 最大の深さを引いて絶対値
        max_number: int = max(node.depth for node in self.nodes)

        for node in self.nodes:
            node.depth = abs(node.depth - max_number)

    def update_nodes(self) -> None:
        """_summary_
            グラフに描画する線分の座標を取得する
        Args:
            depths (List[int]): _description_
        """

        # グラフに書くときのノード初期化

        for node in self.nodes:
            node.start_x = float(node.depth) * self.line_height
            node.start_y = float(len(self.nodes) - node.bnst_id - 1) * self.line_height
            node.end_x = float(node.depth) * self.line_height
            node.end_y = float(len(self.nodes) - node.bnst_id - 1) * self.line_height

        # ノードの数値更新
        for node in self.nodes:

            if node.parent_id == -1:
                continue

            # 終点のx座標 = 係り先の始点のx座標 - self.line_height * 0.5
            node.end_x = self.nodes[node.parent_id].start_x - self.line_height * 0.5

            # 終点のy座標 = 係り先の始点のy座標 + self.line_height * 0.5
            node.end_y = self.nodes[node.parent_id].start_y + self.line_height * 0.5

        # 重複している縦線を削除する
        # 各係り先毎で、最初の要素だけ縦線を残す

        # 係り先となっている文節一覧
        parent_ids = sorted(
            list(set(node.parent_id for node in self.nodes if node.parent_id != -1))
        )

        # parent_ids の各 parent_id に対して、最初に係る文節の bnst_id
        first_bnst_ids: List[int] = [-1 for _ in range(len(parent_ids))]
        for index, parent_id in enumerate(parent_ids):
            for node in self.nodes:
                if node.parent_id == parent_id:
                    first_bnst_ids[index] = node.bnst_id
                    break

        # bnst_id が first_bnst_ids の中に存在しないときは縦線を書かない
        for node in self.nodes:
            if node.bnst_id not in first_bnst_ids:
                node.end_y = node.start_y

    def get_template(self) -> List[str]:
        """_summary_
            標準出力するテキストを作成する
        Args:
            nodes (List[List[float]]): _description_
        """
        return [node.get_template() for node in self.nodes]

    def print_tikz(self) -> None:
        """_summary_
        tikz形式で出力する
        """
        self.get_nest_depth()

        self.update_nodes()

        templates: List[str] = self.get_template()

        output_text: str = (
            "\\begin{tikzpicture}\n" + "".join(templates) + "\\end{tikzpicture}"
        )
        print(output_text)
