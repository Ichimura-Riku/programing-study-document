


from io import TextIOWrapper

def makeTimeTable(busstop_number: int, operation: int, f: TextIOWrapper):
  # ----ここから----



  return
  # ----ここまで-----

ROUTE = ["central", "north", "west", "south"]
for r in ROUTE:
  # ファイルを開く
  with open("../Data/{}.txt".format(r), mode="r", encoding="utf-8") as f:
    # バス停の数
    busstop_number = int(f.readline())
    # バスが一日に走る便数
    operation = int(f.readline())
    print(makeTimeTable(busstop_number, operation, f))
