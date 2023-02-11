# 整数リストnumbersから、乗算結果が最も大きくなる数字を出力する
#
# numbers = [1, -5, 2, 4, -9, 3]の場合、
# 出力は 45

def max_value_mul(numbers: list[int]):
  numbers.sort()
  return max(numbers[0] * numbers[1], numbers[-1] * numbers[-2])

numbers = [1, -5, 2, 4, -9, 3]
print(max_value_mul(numbers))