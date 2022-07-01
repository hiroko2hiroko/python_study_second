#!/usr/bin/env python
# coding: utf-8

# # 1. 配列の種類
# ここでは、list, array, series, dataframeのそれぞれの配列をみていきます。

# ## 1-1. listの例を示します。

# In[ ]:


list1 = [11, 12, 13]
print(list1)


# In[ ]:


list2 = ["A大学", "B大学", "C大学"]
print(list2)


# In[ ]:


list3 =  [123, 'abc', 456.789] 
print(list3)


# In[ ]:


dict1 = {'a':'ABC', 'b':'BCD', 'c': 'CDE'}
print(dict1)


# In[ ]:


tuple1 = ('AB', 12)
print(tuple1)


# **まとめ**
# * list: リスト
# 
#     リストは汎用性が高く、最も使われる配列です。要素の追加・変更・削除が可能で色々な場面で使われます。
# 
#     -  可変(ミュータブル)
#     -  同じ型の要素を格納することが多い
#     -  汎用性が高い
#     -  シーケンスである
#         - シーケンスとは、文字列やリストのような複数の要素をまとめて扱える型のことで、その要素は順序を持ちます。
# 
# 
# * tuple: タプル
# 
#     タプルは、要素を追加・削除・変更することができない配列です。
#     関数の戻り値として複数の要素を一時的に１つにまとめたい場合などでよく使われます。
# 
#     -  不変(イミュータブル)
#     -  複数の型の要素を格納することが多い
#     -  リストよりもメモリを節約できる
#     -  関数の戻り値としてよく使う
#     -  シーケンス型である
# 
# 
# * dict: 辞書
# 
#     辞書は key に value を対応付けて管理する配列です。
#     key に valueを対応付けるためインデックスからではなく key から要素にアクセスできます。
# 
#     -  key と value で1つの要素
#     -  マッピング型である
#     -  連想配列や連想記憶、マップと呼ばれることもある
# <br>
# 
# 

# ## 1-2. arrayの例を示します。

# In[ ]:


ary1 = np.array([["A大学", "B大学", "C大学"],[21, 22, 23]])
print(ary1)
# モジュールがインストールされていないので、エラーが返ってきます。


# In[ ]:


import numpy as np
ary1 = np.array([["A大学", "B大学", "C大学"],[21, 22, 23]])
print(ary1)


# In[ ]:


import numpy as np
ary2 = np.array([[11, 12, 13], [21, 22, 23], [31, 32, 33]])
print(ary2)


# ## 1-3. seriesの例を示します。

# In[ ]:


se1 = pd.Series([10, 11, 12],name='se1')
print(se1)
# モジュールがインストールされていないので、エラーが返ってきます。


# In[ ]:


import pandas as pd
se1 = pd.Series([10, 11, 12],name='se1')
print(se1)


# ## 1-4. dataframeの例を示します。

# In[ ]:


df1 = pd.DataFrame([[100, 101, 102],[200, 201, 202]], columns=['CLM0', 'CLM1', 'CLM2'])
print(df1)
# モジュールがインストールされていないので、エラーが返ってきます。


# In[ ]:


import pandas as pd
df1 = pd.DataFrame([[100, 101, 102],[200, 201, 202]], columns=['CLM0', 'CLM1', 'CLM2'])
print(df1)


# In[ ]:


df1


# In[ ]:


df_x = pd.read_csv(test.csv)
# エラーが返ってきます。ファイルの書き方は注意が必要です。


# In[ ]:


df_x = pd.read_csv("test.csv")
df_x


# In[ ]:


df_ex1 = pd.read_excel("test_excel.xlsx")
df_ex1


# In[ ]:


df_ex2 = pd.read_excel("test_excel.xlsx", sheet_name = "test_sheet2")
df_ex2


# In[ ]:


# google colaboratoryで、google driveに保存してあるファイルを読み込む場合
# １）driveのモジュールをインポート
# from google.colab import drive

# ２）driveのマウント
# drive.mount('/content/drive')

# ３）google drive上でファイルのパスを確認
#  「Data/colaboratory Notebook/test.csv」のパスにあることを確認。

# ４）pandasのread_csvで読み込み
#   「drive/My Drive」以下に、３）で確認したパスを指定して読み込む。
# df_x = pd.read_csv("drive/My Drive/Colaboratory Notebook/test.csv")
# df_x

# excelファイルを開く場合
# １）マウント後にexcel用のモジュールをインストール
# pip install openpyxl
# ２）pandasのread_excelで読み込み
# df_excel2 = pd.read_excel("drive/My Drive/Colaboratory Notebook/test_excel.xlsx", sheet_name = "test_sheet2")
# df_excel2


# # 2. 配列の相互変換
# ここでは、list, array, series, dataframeの相互変換を説明します。

# ## 2-1. listから変換する場合

# In[ ]:


list1 = [11, 12, 13]


# In[ ]:


# arrayに変換
list_array = np.array(list1)
list_array


# In[ ]:


# seriesに変換
list_series = pd.Series(list1)
list_series


# In[ ]:


# dataframeに変換
list_dataframe = pd.DataFrame(list1)
list_dataframe


# ## 2-2. arrayから変換する場合

# In[ ]:


ary1 = np.array([[11, 12, 13], [21, 22, 23], [31, 32, 33]])


# In[ ]:


# listに変換
array_list = ary1.tolist()
array_list


# In[ ]:


# seriesに変換 --->次元エラー
array_series = pd.Series(ary1)
array_series


# In[ ]:


# seriesに変換 ※arrayが1次元の時のみ可能
ary2 = np.array([11, 12, 13])
array_series = pd.Series(ary2)
array_series


# In[ ]:


# dataframeに変換
array_dataframe = pd.DataFrame(ary1)
array_dataframe


# In[ ]:


# dataframeに変換(カラム名の追加)
array_dataframe = pd.DataFrame(ary1, columns=['clm0', 'clm1', 'clm2'])
array_dataframe


# - dataframeでは、カラム名やindex名を指定することができます。
# - オプションを指定する場合は、`columns = []`, `index =[]`を用います。

# ## 2-3. seriesから変換する場合

# In[ ]:


se1 = pd.Series([10, 11, 12],name='se1')


# In[ ]:


# listに変換
series_list = se1.values.tolist()
series_list


# In[ ]:


# arrayに変換
series_array = se1.values
series_array


# In[ ]:


# dataframeに変換
series_dataframe = pd.DataFrame(se1)
series_dataframe


# ## 2-4. dataframeから変換する場合

# In[ ]:


df1 = pd.DataFrame([[100, 101, 102],[200, 201, 202]], columns=['CLM0', 'CLM1', 'CLM2'])


# In[ ]:


# listに変換
dataframe_list = df1.values.tolist()
dataframe_list


# In[ ]:


# arrayに変換
dataframe_array = df1.to_numpy()
dataframe_array


# In[ ]:


# seriesに変換
dataframe_series = df1.iloc[:,0]  # 0列目を指定して抽出
dataframe_series


# # 3. DataFrameの操作

# ## 3-1. 行列操作
# 
# csvやexcelファイルを読み込む際には、インデックスを指定することもできます。

# In[ ]:


df_x = pd.read_csv("test.csv")
df_x


# In[ ]:


df_a = pd.read_csv("test.csv", index_col=0)
df_a


# ## -- 追加（カラム名、インデックス名の変更）

# In[ ]:


df_new = df_a.rename(columns={'B大学': '列名の変更'}, index={'2020年': '行名の変更'})
df_new


# ## -- 追加はここまで

# In[ ]:


# 転置
df_a.T


# In[ ]:


# 列の抽出①
df_a["A大学"]


# In[ ]:


# 列の抽出②
df_a.A大学


# In[ ]:


# 行の抽出①
df_a[1:3]


# In[ ]:


# 行の抽出②
df_a[:3]


# In[ ]:


# 行の抽出③
df_a['2019年':'2021年']


# - locは行名もしくは列名を指定することで特定の値を抽出できます。
# - ilocはindexを指定することで特定の値を抽出できます。つまり、行、列を番号（数字が０のインデックス）で指定します。

# In[ ]:


df_a.loc[:,['B大学','C大学']]


# In[ ]:


df_a.loc['2019年':'2021年',['B大学','C大学']]


# In[ ]:


df_a.iloc[[1,2,4],[0,2]]


# In[ ]:


# 条件を指定して行・列を取得します。
df_a[df_a > 3001]


# In[ ]:


# 行の削除
df_a.drop('2021年', axis=0)


# In[ ]:


# 列の削除
df_a.drop('D大学', axis=1)


# ## 3-1. データの結合

# In[ ]:


df_a = pd.read_csv("test.csv", index_col=0)
df_a


# In[ ]:


df_b = pd.read_csv("test_add1.csv", index_col=0)
df_b


# In[ ]:


df_c = pd.read_csv("test_add2.csv", index_col=0)
df_c


# In[ ]:


# 横結合
# インデックス（行ラベル）をキーに指定する場合は、引数left_index, right_indexをTrueとする。
pd.merge(df_a, df_b, left_index=True, right_index=True)


# In[ ]:


# 縦結合
pd.concat([df_a, df_c])


# # 4. 欠損値の補完

# In[ ]:


import numpy as np
from numpy import nan as NA
import pandas as pd

df_miss = pd.read_csv("test_miss.csv", index_col=0)
df_miss


# In[ ]:


# 欠損値有無の確認
df_miss.isnull().sum()


# In[ ]:


# リストワイズ削除
# NaNのある行を全て削除
df_miss.dropna()


# In[ ]:


# fillna(値)で埋める
df_miss.fillna(0)


# In[ ]:


# 前の値で埋める
df_miss.fillna(method = 'ffill') 
# 後ろの値で埋める
# df_miss.fillna(method = 'bfill') 


# In[ ]:


# 前後の値から予測する
df_miss.interpolate()


# In[ ]:


# 平均で埋める
# 平均値
df_miss.mean()


# In[ ]:


# 平均値で埋める
df_miss.fillna(df_miss.mean())


# In[ ]:




