#-*- coding:utf-8 -*-
from fractions import gcd


class RatNum(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.gcd_filter()
        return

    def gcd_filter(self):

        common_gcd = gcd(self.a, self.b)
        self.a /= common_gcd
        self.b /= common_gcd
        return
    

    def __sub__(self, rat_num_):

        rat_num = RatNum(0, 1)
        rat_num.a = self.a * rat_num_.b - self.b * rat_num_.a
        rat_num.b = self.b * rat_num_.b
        rat_num.gcd_filter()
        return rat_num

    def __add__(self, rat_num_):
        rat_num = RatNum(0, 1)
        rat_num.a = self.a * rat_num_.b + self.b * rat_num_.a
        rat_num.b = self.b * rat_num_.b
        rat_num.gcd_filter()
        return rat_num
        
    def __mul__(self, rat_num_):
        rat_num = RatNum(0, 1)
        rat_num.a = self.a * rat_num_.a
        rat_num.b = self.b * rat_num_.b
        rat_num.gcd_filter()
        return rat_num

    def __div__(self, rat_num_):
        rat_num = RatNum(0, 1)
        rat_num.a = self.a * rat_num_.b
        rat_num.b = self.b * rat_num_.a
        rat_num.gcd_filter()
        return rat_num

    def __neg__(self,):
        rat_num = RatNum(0, 1)
        rat_num.a = self.a * (-1)
        rat_num.b = self.b
        rat_num.gcd_filter()
        return rat_num

    def show(self):
        print "%s/%s"%(self.a, self.b)
        return

def test_ratnum():
    """
    """
    print "[Test RatNum]"
    print "Test RatNum +"
    rat_a = RatNum(3, 5)
    rat_b = RatNum(4, 7)
    rat_c = rat_a + rat_b
    rat_c.show()

    print "Test RatNum gcd filter"
    rat_a = RatNum(2, 4)
    rat_b = RatNum(3, 6)
    rat_c = rat_a + rat_b
    rat_c.show()

    print "Test RatNum * and /"
    (rat_a * rat_b).show()
    (rat_a / rat_b).show()

    return


if __name__ == "__main__":
    test_ratnum()
