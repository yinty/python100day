import time

class Colck(object):

    def __init__(self,hour=0, minute=0, second=0):
        """
        构造器

        :param hour: 时
        :param minute: 分
        :param second: 秒
        """
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        
        self._second +=1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute ==60:
                self._minute = 0
                self._hour += 1
                if self._hour ==24:
                    self._hour = 0

    def __str__(self):
        """显示时间"""
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)

def main():
    colck = Colck(23,58,59)
    while True:
        print(colck)
        time.sleep(1)
        colck.run()

if __name__ == '__main__':
    main()

