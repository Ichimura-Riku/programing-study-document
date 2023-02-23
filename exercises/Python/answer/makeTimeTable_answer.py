


from io import TextIOWrapper

def makeTimeTable(busstop_number: int, operation: int, f: TextIOWrapper):
  # ----ここから----
  result = []
  # for _ in range(busstop_number):
  for time in f.readlines():
    h, m = map(int, time.split(' '))
    timetable = []
    for _ in range(operation):
      timetable.append(f"{h:02}:{m:02}")
      if m >= 10:
        m -= 10
        h += 1
      else :
        m += 50
    result.append(timetable)
  return result
  # ----ここまで----

ROUTE = ["central", "north", "west", "south"]
for r in ROUTE:
  # ファイルを開く
  with open("../../data/{}.txt".format(r), mode="r", encoding="utf-8") as f:
    busstop_number = int(f.readline())
    operation = int(f.readline())
    print(makeTimeTable(busstop_number, operation, f))

