# 解答例
def sort_value(items: list[dict()]):
  sort_items = sorted(items, key=lambda x: x["value"], reverse=True)
  return sort_items

# 解答例2
def sort_value2(items: list[dict]):
  for i in range(len(items)):
    items[i]["value"]


  return

items = [
  { "value": 500, "weight": 8 },
  { "value": 400, "weight": 5 },
  { "value": 350, "weight": 4 },
  { "value": 700, "weight": 10 }
]
print(sort_value(items))