# tikz-cabocha-format
形態素解析の結果をcabocha formatでlatexに出力するためのtikzコードを生成する

## 例

### 対象の文

```plain
私は自然言語処理の勉強をしています
```

### 入力形式
```
List[見出し,文節番号(0-index),係り先文節番号(0-index)]
```

### 入力
ヘッダーなしcsv形式ファイル(例: `./csvs/sample.csv`)

```plain
私は,0,3
自然言語処理の,1,2
勉強を,2,3
しています,3,-1
```

### 実行コマンド
```
python3 main.py [ファイルのパス]
```

実行例
```
python3 main.py ./csvs/sample.csv
```

### 出力コード

```plain
\begin{tikzpicture}
    \draw[thick]  (1.0,3.0) -| (1.5,0.5) node [pos=0, anchor=east] {私は};
    \draw[thick]  (0.0,2.0) -| (0.5,1.5) node [pos=0, anchor=east] {自然言語処理の};
    \draw[thick]  (1.0,1.0) -| (1.5,1.0) node [pos=0, anchor=east] {勉強を};
    \draw[thick]  (2.0,0.0) -| (2.0,0.0) node [pos=0, anchor=east] {しています};
\end{tikzpicture}
```

### Latex 出力例

![image](https://user-images.githubusercontent.com/44014265/207295760-d0f4ca34-fe63-4f61-b4ea-535dad855047.png)
