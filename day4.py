"""

用for循环实现1~100求和

Version: 0.1
Author: 骆昊
Date: 2018-03-01

"""

sum = 0
for x in range(101):
    sum += x
print(sum)
"""

用for循环实现1~100之间的偶数求和

Version: 0.1
Author: 骆昊
Date: 2018-03-01

"""
sum = 0
for x in range(2, 101, 2):
    sum +=x
print(sum)

for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j), end='\t')
    print()

row = int(input('请输入行数: '))
for i in range(row):
    for _ in range(i + 1):
        print('*', end='')
    print()



"""

猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了

Version: 0.1
Author: 骆昊
Date: 2018-03-01

"""
import random

answer = random.randint(1,100)
counter = 0
while True:
    counter +=1
    number = int(input('请输入：'))
    if number < answer:
        print('大一点')
    elif number > answer:
        print('小一点')
    else:
        print('恭喜你猜对了!')
        break
print('你一共猜了%d次' % counter)
if counter > 7:
    print('你的智商余额明显不足')