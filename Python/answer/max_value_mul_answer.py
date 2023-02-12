# 整数リストnumbersから、乗算結果が最も大きくなる数字を出力する
#
# numbers = [1, -5, 2, 4, -9, 3]の場合、
# 出力は 45


# 解答例1
# スマートなやり方(後で見せる)
def max_value_mul(numbers: list[int]):
  numbers.sort()
  return max(numbers[0] * numbers[1], numbers[-1] * numbers[-2])

# 解答例2
# 愚直なやり方
def max_value_mul2(numbers: list[int]):
  ans = 0
  max_val = max(numbers)
  min_val = min(numbers)
  for index, num in enumerate(numbers):
    if numbers.index(max_val) == index or numbers.index(min_val) == index:
      continue
    
    if ans < min_val * num:
      ans = min_val * num
    elif ans < max_val * num:
      ans = max_val * num

  return ans

numbers = [1, -5, 2, 4, -9, 3]
print(max_value_mul2(numbers))