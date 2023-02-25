# 全体確認用の問題
# 総復習として、バグ修正の問題に取り組んでみよう
# 時間が余ればもっと良くなるように考えてみよう

a = 5
b = `春休み勉強会`
c = ['第1回', '第2回', '第3回',]
d = ['復習', 'ちょいテク', '未定']

print(b)
print()
for i in renge(a):
    print(f'{C[i]}は' + f'{d[i]} の回')

while True:
   print('予定を修正する？')
    e = imput('True/Falseで入力')
    f = imput('第何回を？')
    if e :
        d[f] = input('変更する内容を記述')
        print(b)
        print()
        for i in renge(a):
            print(f'{C[i]}は' + f'{d[i]} の回')
    else:
        break



