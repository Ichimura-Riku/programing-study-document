import random
data = [
  ["central", "data1", "data2", "data3"],
  ["nonkey", "data1", "data2"],
  ["north", "data1", "data2"],
  ["south", "data1", "data2", "data3"],
  ["west", "data1", "data2", "data3", "data4"]
]
def sort_route(data: list[list[str]]):
  routes = ["central", "south", "west", "north", "nonkey"]
  result = [[],[],[],[],[]]
  for d in data:
    result[routes.index(d[0])] = d
  return result

# シャッフルします ^o^
random.shuffle(data)
print("<変更前>")
for x in data:
  print(x)
print("<変更後>")
answer = sort_route(data)
for x in answer:
  print(x)