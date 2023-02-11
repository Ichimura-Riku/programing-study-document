# 整数リストnumbersから、最も大きい数を出力する

# 解答例
def max_value(numbers: list[int]):
  return max(numbers)

# 解答例2
def max_value2(numbers: list[int]):
  maximum = 0
  for num in numbers:
    if (maximum < num):
      maximum = num
  return maximum

numbers = [1, 4, 5, 7, 8, 4, 35, 2, 12124, 2]
max_value(numbers)