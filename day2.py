# coding=utf-8
"""变量和类型

在程序设计中，变量是一种存储数据的载体。计算机中的变量是实际存在的数据或者说是存储器中存储数据的一块内存空间，变量的值可以被读取和修改，这是所有计算和控制的基础。计算机能处理的数据有很多中类型，除了数值之外还可以处理文本、图形、音频、视频等各种各样的数据，那么不同的数据就需要定义不同的存储类型。Python中的数据类型很多，而且也允许我们自定义新的数据类型（这一点在后面会讲到），我们先介绍几种常用的数据类型。"""
print('I\'m \"OK\"!')
print('I\'m learning\nPython')
print(10/3)
print('包含中文的str')
print(ord('A'))
print(ord('中'))

a = 321
b = 123
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

a = int(input('a= '))
b = int(input('b= '))
print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %f' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))

"""

使用type()检查变量的类型

Version: 0.1
Author: yinty
Date: 2018-02-27

"""
a = 100
b = 12.345
c = 1 + 5j
d = 'hello, world'
e = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))

import math
redius = float(input('请输入圆的半径：'))
perimeter = 2 * math.pi * redius
area = math.pi * redius * redius
print('周长：%.2f' % perimeter)
print('面积：%.2f' % area)

year = int (input('请输入年份：'))
is_leap = (year % 4==0 and year % 100 != 0 or year %400 ==0)
print(is_leap)
