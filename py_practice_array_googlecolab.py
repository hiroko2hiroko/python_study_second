# -*- coding: utf-8 -*-
"""py_practice_array_googlecolab.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TTT-6KQnPIii5qlaNAJ8Uc4kgaKOoi6w

# 1. 配列の種類
ここでは、list, array, series, dataframeのそれぞれの配列をみていきます。

## 1-1. listの例を示します。
"""

list1 = [11, 12, 13]
print(list1)

list2 = ["A大学", "B大学", "C大学"]
print(list2)

list3 =  [123, 'abc', 456.789] 
print(list3)

dict1 = {'a':'ABC', 'b':'BCD', 'c': 'CDE'}
print(dict1)

tuple1 = ('AB', 12)
print(tuple1)

"""**まとめ**
* list: リスト

    リストは汎用性が高く、最も使われる配列です。要素の追加・変更・削除が可能で色々な場面で使われます。

    -  可変(ミュータブル)
    -  同じ型の要素を格納することが多い
    -  汎用性が高い
    -  シーケンスである
        - シーケンスとは、文字列やリストのような複数の要素をまとめて扱える型のことで、その要素は順序を持ちます。


* tuple: タプル

    タプルは、要素を追加・削除・変更することができない配列です。
    関数の戻り値として複数の要素を一時的に１つにまとめたい場合などでよく使われます。

    -  不変(イミュータブル)
    -  複数の型の要素を格納することが多い
    -  リストよりもメモリを節約できる
    -  関数の戻り値としてよく使う
    -  シーケンス型である


* dict: 辞書

    辞書は key に value を対応付けて管理する配列です。
    key に valueを対応付けるためインデックスからではなく key から要素にアクセスできます。

    -  key と value で1つの要素
    -  マッピング型である
    -  連想配列や連想記憶、マップと呼ばれることもある
<br>

## 1-2. arrayの例を示します。
"""

ary1 = np.array([["A大学", "B大学", "C大学"],[21, 22, 23]])
print(ary1)
# モジュールがインストールされていないので、エラーが返ってきます。

import numpy as np
ary1 = np.array([["A大学", "B大学", "C大学"],[21, 22, 23]])
print(ary1)

import numpy as np
ary2 = np.array([[11, 12, 13], [21, 22, 23], [31, 32, 33]])
print(ary2)

"""## 1-3. seriesの例を示します。"""

se1 = pd.Series([10, 11, 12],name='se1')
print(se1)
# モジュールがインストールされていないので、エラーが返ってきます。

import pandas as pd
se1 = pd.Series([10, 11, 12],name='se1')
print(se1)

"""## 1-4. dataframeの例を示します。"""

df1 = pd.DataFrame([[100, 101, 102],[200, 201, 202]], columns=['CLM0', 'CLM1', 'CLM2'])
print(df1)
# モジュールがインストールされていないので、エラーが返ってきます。

import pandas as pd
df1 = pd.DataFrame([[100, 101, 102],[200, 201, 202]], columns=['CLM0', 'CLM1', 'CLM2'])
print(df1)

df1

"""## 1-5. google driveに保存してあるファイルの読み込み


*   driveのモジュールをインポート
    - `from google.colab import drive`
*   driveのマウント
    - `drive.mount('/content/drive')`
*   google drive上でファイルのパスを確認
    - `Data/colaboratory Notebook/test.csv`のパスにあることを確認。
*   pandasのread_csvで読み込み
    - `drive/My Drive`以下に、３）で確認したパスを指定して読み込む。
    - `df_x = pd.read_csv("drive/My Drive/Colaboratory Notebook/test.csv")`



"""

from google.colab import drive
drive.mount('/content/drive')

df_x = pd.read_csv("drive/My Drive/Colaboratory Notebook/test.csv")
df_x

"""excelファイルを開く場合
*   マウント後にexcel用のモジュールをインストール
    - `pip install openpyxl`
*   pandasのread_excelで読み込み
    - `df_excel2 = pd.read_excel("drive/My Drive/Colaboratory Notebook/test_excel.xlsx", sheet_name = "test_sheet2")`
*   表示
    - `df_excel2`

# 2. 配列の相互変換
ここでは、list, array, series, dataframeの相互変換を説明します。

## 2-1. listから変換する場合
"""

list1 = [11, 12, 13]

# arrayに変換
list_array = np.array(list1)
list_array

# seriesに変換
list_series = pd.Series(list1)
list_series

# dataframeに変換
list_dataframe = pd.DataFrame(list1)
list_dataframe

"""## 2-2. arrayから変換する場合"""

ary1 = np.array([[11, 12, 13], [21, 22, 23], [31, 32, 33]])

# listに変換
array_list = ary1.tolist()
array_list

# seriesに変換 --->次元エラー
array_series = pd.Series(ary1)
array_series

# seriesに変換 ※arrayが1次元の時のみ可能
ary2 = np.array([11, 12, 13])
array_series = pd.Series(ary2)
array_series

# dataframeに変換
array_dataframe = pd.DataFrame(ary1)
array_dataframe

# dataframeに変換(カラム名の追加)
array_dataframe = pd.DataFrame(ary1, columns=['clm0', 'clm1', 'clm2'])
array_dataframe

"""- dataframeでは、カラム名やindex名を指定することができます。
- オプションを指定する場合は、`columns = []`, `index =[]`を用います。

## 2-3. seriesから変換する場合
"""

se1 = pd.Series([10, 11, 12],name='se1')

# listに変換
series_list = se1.values.tolist()
series_list

# arrayに変換
series_array = se1.values
series_array

# dataframeに変換
series_dataframe = pd.DataFrame(se1)
series_dataframe

"""## 2-4. dataframeから変換する場合"""

df1 = pd.DataFrame([[100, 101, 102],[200, 201, 202]], columns=['CLM0', 'CLM1', 'CLM2'])

# listに変換
dataframe_list = df1.values.tolist()
dataframe_list

# arrayに変換
dataframe_array = df1.to_numpy()
dataframe_array

# seriesに変換
dataframe_series = df1.iloc[:,0]  # 0列目を指定して抽出
dataframe_series

"""# 3. DataFrameの操作

## 3-1. 行列操作

csvやexcelファイルを読み込む際には、インデックスを指定することもできます。
"""

df_x = pd.read_csv("drive/My Drive/Colaboratory Notebook/test.csv")
df_x

df_a = pd.read_csv("drive/My Drive/Colaboratory Notebook/test.csv", index_col=0)
df_a

"""## -- 追加（カラム名、インデックス名の変更）"""

df_new = df_a.rename(columns={'B大学': '列名の変更'}, index={'2020年': '行名の変更'})
df_new

"""## -- 追加はここまで"""

# 転置
df_a.T

# 列の抽出①
df_a["A大学"]

# 列の抽出②
df_a.A大学

# 行の抽出①
df_a[1:3]

# 行の抽出②
df_a[:3]

# 行の抽出③
df_a['2019年':'2021年']

"""- locは行名もしくは列名を指定することで特定の値を抽出できます。
- ilocはindexを指定することで特定の値を抽出できます。つまり、行、列を番号（数字が０のインデックス）で指定します。
"""

df_a.loc[:,['B大学','C大学']]

df_a.loc['2019年':'2021年',['B大学','C大学']]

df_a.iloc[[1,2,4],[0,2]]

# 条件を指定して行・列を取得します。
df_a[df_a > 3001]

# 行の削除
df_a.drop('2021年', axis=0)

# 列の削除
df_a.drop('D大学', axis=1)

"""## 3-1. データの結合"""

df_a = pd.read_csv("drive/My Drive/Colaboratory Notebook/test.csv", index_col=0)
df_a

df_b = pd.read_csv("drive/My Drive/Colaboratory Notebook/test_add1.csv", index_col=0)
df_b

df_c = pd.read_csv("drive/My Drive/Colaboratory Notebook/test_add2.csv", index_col=0)
df_c

# 横結合
# インデックス（行ラベル）をキーに指定する場合は、引数left_index, right_indexをTrueとする。
pd.merge(df_a, df_b, left_index=True, right_index=True)

# 縦結合
pd.concat([df_a, df_c])

"""# 4. 欠損値の補完"""

import numpy as np
from numpy import nan as NA
import pandas as pd

from google.colab import drive
drive.mount('/content/drive')

df_miss = pd.read_csv("drive/My Drive/Colaboratory Notebook/test_miss.csv", index_col=0)
df_miss

# 欠損値有無の確認
df_miss.isnull().sum()

# リストワイズ削除
# NaNのある行を全て削除
df_miss.dropna()

# fillna(値)で埋める
df_miss.fillna(0)

# 前の値で埋める
df_miss.fillna(method = 'ffill') 
# 後ろの値で埋める
# df_miss.fillna(method = 'bfill')

# 前後の値から予測する
df_miss.interpolate()

# 平均で埋める
# 平均値
df_miss.mean()

# 平均値で埋める
df_miss.fillna(df_miss.mean())
