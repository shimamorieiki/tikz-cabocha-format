# tikz-cabocha-format
係り受け解析の結果をcabocha formatでlatexに出力するためのtikzコードを生成する

## 例

### 必要なlatexのpackage
- tikz

### 対象の文

```plain
私は自然言語処理の勉強をしています
```

### 入力形式
```
List[見出し,文節番号(0-index),係り先文節番号(0-index)]
```
- 係り先が存在しない(=文末に相当する)文節の係り先文節番号は-1とする

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
python3 main.py [ファイルのパス] [オプション(行の高さ)]
```

行の高さは `-xlarge`, `-large`, `-middle`, `-small`の四種(省略時は`"-xlarge"`相当)

実行例
```
python3 main.py ./csvs/sample.csv -xlarge
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

#### -xlarge
![xlarge](https://user-images.githubusercontent.com/44014265/211229082-b40e5faa-3b02-40cb-a31f-a39537435e0f.png)


#### -large
![large](https://user-images.githubusercontent.com/44014265/211229094-a57d1f49-e035-4ffc-822e-d72870b9cefe.png)


#### -middle
![middle](https://user-images.githubusercontent.com/44014265/211229099-61f5be08-4bea-4dcd-a006-8628dbfea258.png)


#### -small
![small](https://user-images.githubusercontent.com/44014265/211229115-dde43ac1-4202-432f-8375-7241c2d8d4fc.png)

