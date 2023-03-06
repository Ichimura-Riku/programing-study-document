# 問題
# 中央、のんキー、北部、南部、西部のデータが順番がランダムで入った配列dataが入力される。
# アプリ内で使う時は、中央、南部、西部、北部、のんキーの順番にしたい。
# 
# dataは1例として、以下のような形となっている。
# data = [
#   ["central", "data1", "data2", "data3"],
#   ["nonkey", "data1", "data2"],
#   ["north", "data1", "data2"],
#   ["south", "data1", "data2", "data3"],
#   ["west", "data1", "data2", "data3", "data4"]
# ]
# これを 
# [
#   ["central", "data1", "data2", "data3"],
#   ["south", "data1", "data2", "data3"],
#   ["west", "data1", "data2", "data3", "data4"],
#   ["north", "data1", "data2"],
#   ["nonkey", "data1", "data2"]
# ]
# というように並び替える  

import random
data = [
  ["central", "data1", "data2", "data3"],
  ["nonkey", "data1", "data2"],
  ["north", "data1", "data2"],
  ["south", "data1", "data2", "data3"],
  ["west", "data1", "data2", "data3", "data4"]
]

def sort_route(data: list[list[str]]):
  # ----ここから----



  
  return
  # ----ここまで----

# シャッフルします ^o^
random.shuffle(data)
print("<変更前>")
for x in data:
  print(x)
print("<変更後>")
answer = sort_route(data)
for x in answer:
  print(x)