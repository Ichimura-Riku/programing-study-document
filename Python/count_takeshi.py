# 文字列リストclassmateから、"たけし"君が何人いるか出力する

# 解答例
def count_takeshi(classmates: list[str]):
  return classmates.count("たけし")

# 解答例2
def count_takeshi2(classmates: list[str]):
  count = 0
  for classmate in classmates:
    if (classmate == "たけし"):
      count+=1
  return count

classmates = ["たけし", "こけし", "たろう", "たけと", "たけし", "たにし", "たいじ", "たけしん", "ばなな" ]
print(count_takeshi(classmates))