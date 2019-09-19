###定义类

class Student(object):

    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在学习%s.' %(self.name,course_name))

# PEP 8要求标识符的名字用全小写多个单词用下划线连接
# 但是很多程序员和公司更倾向于使用驼峰命名法(驼峰标识)

    def watch_av(self):
        if self.age < 18:
            print('%s只能观看《熊出没》.' %self.name)
        else:
            print('%s正在观看岛国爱情片》' %self.name)


### 创建和使用对象
###当我们定义好一个类之后，可以通过下面的方式来创建对象并给对象发消息。

def main():
    # 创建学生对象并指定姓名和年龄
    stu1 = Student('阴庭宇', 23)
    # 给对象发study消息
    stu1.study('Python程序设计')
    #给对象发wathch_av消息
    stu1.watch_av()
    stu2 = Student('王大锤', 34)
    stu2.study('思想品德')
    stu2.watch_av()

if __name__ == '__main__':
    main()
