import numpy as np

# np.array() 関数による生成
## リストから生成
list_a = np.array([1, 2, 3])
print("list_a", list_a)

## タプルから生成
tupple_a = np.array((10, 20, 30))
print("tupple_a", tupple_a)

## 2重にネストしたリストから生成
list_b = np.array([[1.5, 0], [0, 3.0]])
print("list_b", list_b)

## リストの要素に np.ndarray やタプルを含んで生成
list_c = np.array([1.0, 2.0, 3.0])
list_d = np.array([list_c, (4.0, 5.0, 6.0)])
print("list_d", list_d)


# その他の関数による生成
## np.zerosによる生成
zeros_a = np.zeros(3)  # 0で初期化された要素数3の1次元配列
print("zeros_a", zeros_a)
zeros_b = np.zeros((2, 3))  # 0で初期化された2x3の2次元配列
print("zeros_b", zeros_b)

## np.onesによる生成
ones_a = np.ones(3)  # 1で初期化された要素数3の1次元配列
print("one_a", ones_a)
ones_b = np.ones((3, 4))  # 1で初期化された3x4の2次元配列
print("ones_b", ones_b)

## np.empty による生成
empty_a = np.empty(3000)  # 初期化されていない要素数3の1次元配列
print("empty_a", empty_a)  # 内容は不定

## np.zeros_like による生成
zeros_like_a = np.zeros_like(list_c)  # list_cと同じ形状で0で初期化された配列
print("zeros_like_a", zeros_like_a)

## identity による生成
identity_a = np.identity(3)  # 3x3の単位行列
print("identity_a", identity_a)


# NumPy 配列の属性と要素の参照

## 整数のリストをもとに、float64 で生成する
list_a = np.array([1, 2, 3])
print("list_a dtype", list_a, list_a.dtype)  # int64
list_a = np.array([1, 2, 3], dtype=np.float64)
print("list_a dtype", list_a, list_a.dtype)  # float64

## 浮動小数点型の配列を複素数型で作り直す
list_a = np.array([1.0, 1.5, 2.0])
print(list_a, list_a.dtype)  # float64

list_a = np.array(list_a, dtype=complex)
print(list_a, list_a.dtype)  # complex128

## astype で型を変換する
list_a = np.array([1, 2, 3])
print("astype", list_a, list_a.dtype, list_a.astype(float), list_a.astype(float).dtype)

# 要素の参照方法

## 1次元配列の場合
list_a = np.array([1, 2, 3, 4, 5], dtype=float)
print(list_a[3])  # 4.0 (添字はゼロスタート)

## 2次元配列の場合
list_b = np.array([[1, 2, 3], [4, 5, 6]], dtype=float)
print(list_b.shape, list_b[1, 2])  # 6.0 (添字はゼロスタート)


# ベクトルの行列との関係 (ネストしたリストを用いて生成)

## 縦ベクトル
list_a = np.array([[1], [2], [3]])  # 3x1の行列
print("縦ベクトル", list_a)

## 横ベクトル
list_b = np.array([[1, 2, 3]])  # 1x3の行列
print("横ベクトル", list_b)
