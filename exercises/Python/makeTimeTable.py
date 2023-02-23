# 時刻表を作成しよう
# 
# 入力: 
# バス停の数 busstop_number: 整数
# バスが一日に走る便数 operation: 整数
# 時刻表の一部のデータを持ったファイル f: f = open(ファイル)したやつ

# 詳しい情報
# 時刻表データは、f.readline()で一行読むと、
# 6 50
# のようなデータが得られる。
# これは1つ目のバス停の始発が6時50分であることを表す。
# 次にf.readline()をすると、
# 6 51
# のようなデータになる。
# これは2つ目のバス停の始発が6時51分であることを表す。

# また、次のバスは50分間隔で来ることがわかっている。


# 期待する出力
# そのルートの時刻表をまとめた2重配列
# 列数: operation
# 行数: busstop_number
# 例:
# [
#   ["06:50", "07:40", "08:30", ...省略... , "19:20"], 
#   ...省略...
#   [busstop_number番目のバス停の時刻表]
# ]
#





from io import TextIOWrapper

def makeTimeTable(busstop_number: int, operation: int, f: TextIOWrapper):
  # ----ここから----
  


  return 
  # ----ここまで----

ROUTE = ["central", "north", "west", "south"]
for r in ROUTE:
  # ファイルを開く
  with open("../data/{}.txt".format(r), mode="r", encoding="utf-8") as f:
    # バス停の数
    busstop_number = int(f.readline())
    # バスが一日に走る便数
    operation = int(f.readline())
    print(makeTimeTable(busstop_number, operation, f))
