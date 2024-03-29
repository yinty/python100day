## 面向对象进阶

##在前面的章节我们已经了解了面向对象的入门知识，
# 知道了如何定义类，如何创建对象以及如何给对象
# 发消息。为了能够更好的使用面向对象编程思想进行程序开发，
# 我们还需要对Python中的面向对象编程进行更为深入的了解。

### @property装饰器

##之前我们讨论过Python中属性和方法访问权限的问题
#，虽然我们不建议将属性设置为私有的，但是如果直接将属性
# 暴露给外界也是有问题的，比如我们没有办法检查赋给属性的
# 值是否有效。我们之前的建议是将属性命名以单下划线开头，
# 通过这种方式来暗示属性是受保护的，不建议外界直接访问，
# 那么如果想访问属性可以通过属性的getter（访问器）
# 和setter（修改器）方法进行对应的操作。如果要做到这点，
# 就可以考虑使用@property包装器来包装getter和setter方法，
#使得对属性的访问既安全又方便，代码如下所示。
'''
class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    #访问器 - getter方法
    @property
    def name(self):
        return self._name

    #访问器 - getter方法
    @property
    def age(self):
        return self._age

    #修改器 - setter方法
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <=16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


def main():
    person = Person('王大锤', 12)
    person.play()
    person.age = 22
    person.play()

if __name__ == '__main__':
    main()
'''


### \_\_slots\_\_魔法

#我们讲到这里，不知道大家是否已经意识到，Python是一门[动态语言]
# (https://zh.wikipedia.org/wiki/%E5%8A%A8%E6%80%
# 81%E8%AF%AD%E8%A8%80)。通常，动态语言允许我们在程
# 序运行时给对象绑定新的属性或方法，当然也可以对已经绑定的属
# 性和方法进行解绑定。但是如果我们需要限定自定义类型的对象只
# 能绑定某些属性，可以通过在类中定义\_\_slots\_\_变量来进行限
# 定。需要注意的是\_\_slots\_\_的限定只对当前类的对象
# 生效，对子类并不起任何作用。

'''class Person(object):

    # 限定Person对象只能绑定_name, _age和_gender属性
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


def main():
    person = Person('王大锤', 22)
    person.play()
    person._gender = '男'
    # AttributeError: 'Person' object has no attribute '_is_gay'
    person._is_gay = True

if __name__ == '__main__':
    main()

'''

### 静态方法和类方法

#之前，我们在类中定义的方法都是对象方法，也就是说这些方法都是
# 发送给对象的消息。实际上，我们写在类中的方法并不需要都是对象
# 方法，例如我们定义一个“三角形”类，通过传入三条边长来构造三角
# 形，并提供计算周长和面积的方法，但是传入的三条边长未必能构造
# 出三角形对象，因此我们可以先写一个方法来验证三条边长是否可以
# 构成三角形，这个方法很显然就不是对象方法，因为在调用这个方法
# 时三角形对象尚未创建出来（因为都不知道三条边能不能构成三角形
# ），所以这个方法是属于三角形类而并不属于三角形对象的。我们可
# 以使用静态方法来解决这类问题，代码如下所示。

'''from math import sqrt

class Triangle(object):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c
    
    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and b + c > a and a + c > b
    
    def perimeter(self):
        return self._a + self._b +self._c
    
    def area(self):
        half = self.perimeter() / 2
        return sqrt(half *(half - self._a) * (half - self._b) * (half - self._c))

def main():
    a, b, c = 3, 4, 5
    # 静态方法和类方法都是通过给类发消息来调用的
    if Triangle.is_valid(a, b, c):
        t = Triangle(a, b, c)
        print(t.perimeter())
        # 也可以通过给类发消息来调用对象方法但是要传入接收消息的对象作为参数
        # print(Triangle.perimeter(t))
        print(t.area())
        # print(Triangle.area(t))
    else:
        print('无法构成三角形.')

if __name__ == '__main__':
    main()
'''

#和静态方法比较类似，Python还可以在类中定义类方法，类方法的第
# 一个参数约定名为cls，它代表的是当前类相关的信息的对象（类本身
# 也是一个对象，有的地方也称之为类的元数据对象），通过这个参数
# 我们可以获取和类相关的信息并且可以创建出类的对象，代码如下所示。
'''
from time import time, localtime, sleep

class Clock(object):
    """数字时钟"""

    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

    def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """显示时间"""
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)


def main():
    # 通过类方法创建对象并获取系统时间
    clock = Clock.now()
    while True:
        print(clock.show())
        sleep(1)
        clock.run()


if __name__ == '__main__':
    main()
'''

### 类之间的关系

#简单的说，类和类之间的关系有三种：is-a、has-a和use-a关系。

#- is-a关系也叫继承或泛化，比如学生和人的关系、手机和电子产品的关系都属于继承关系。
#- has-a关系通常称之为关联，比如部门和员工的关系，汽车和引擎的关系都属于关联关系；关联关系如果是整体和部分的关联，那么我们称之为聚合关系；如果整体进一步负责了部分的生命周期（整体和部分是不可分割的，同时同在也同时消亡），那么这种就是最强的关联关系，我们称之为合成关系。
#- use-a关系通常称之为依赖，比如司机有一个驾驶的行为（方法），其中（的参数）使用到了汽车，那么司机和汽车的关系就是依赖关系。

#利用类之间的这些关系，我们可以在已有类的基础上来完成某些操作，也可以在已有类的基础上创建新的类，这些都是实现代码复用的重要手段。复用现有的代码不仅可以减少开发的工作量，也有利于代码的管理和维护，这是我们在日常工作中都会使用到的技术手段。

'''
class Person(object):
    #人

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._sge = age
    
    def play(self):
        print('%s正在愉快的玩耍.' % self._name)

    def watch_av(self):
        if self.age >= 18:
            print('%s正在观看爱情动作片.' %self._name)
        else:
            print('%s只能观看《熊出没》.' %self._name)


class Student(Person):
    #学生

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade
    
    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print('%s的%s正在学习%s.' %(self._grade, self._name, course))


class Teacher(Person):
    #老师

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(slef):
        return self._title
    
    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print('%s%s正在讲%s.' %(self._name, self._title, course))


def main():
    stu = Student('王大锤', 15, '初三')
    stu.study('数学')
    stu.watch_av()
    t = Teacher('阴庭宇', 23, '老叫兽')
    t.teach('Python程序设计')
    t.watch_av()

if __name__ == '__main__':
    main()

'''
#子类在继承了父类的方法后，可以对父类已有的方法给出新的实现版本
#，这个动作称之为方法重写（override）。通过方法重写我们可以让
#父类的同一个行为在子类中拥有不同的实现版本，当我们调用这个经过
#子类重写的方法时，不同的子类对象会表现出不同的行为，这个就是
#多态（poly-morphism）。

from abc import ABCMeta, abstractclassmethod

class Pet(object, metaclass=ABCMeta):
    #宠物

    def __init__(self, nickname):
        self._nickname = nickname

    @abstractclassmethod
    def make_voice(self):
        #发出声音
        pass

class Dog(Pet):
    #狗

    def make_voice(self):
        print('%s:汪汪汪... ' % self._nickname)

class Cat(Pet):
    #猫

    def make_voice(self):
        print('%s: 喵...喵...' % self._nickname)

def main():
    pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄')]
    for pet in pets:
        pet.make_voice()

if __name__ == "__main__":
    main()

#在上面的代码中，我们将`Pet`类处理成了一个抽象类，所谓抽象类
# 就是不能够创建对象的类，这种类的存在就是专门为了让其他类去
# 继承它。Python从语法层面并没有像Java或C#那样提供对抽象类
# 的支持，但是我们可以通过`abc`模块的`ABCMeta`元类和
# `abstractmethod`包装器来达到抽象类的效果，如果一个类中
# 存在抽象方法那么这个类就不能够实例化（创建对象）。上面的
# 代码中，`Dog`和`Cat`两个子类分别对`Pet`类中的`make_voic
# e`抽象方法进行了重写并给出了不同的实现版本，当我们在`main
# `函数中调用该方法时，这个方法就表现出了多态行为（同样的方法
# 做了不同的事情）。




