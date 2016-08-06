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

    def to_num(self):
        return self.a * 1.0 / self.b

    def show(self):
        print "%s/%s"%(self.a, self.b)
        return



class RatPoint(object):
    def __init__(self,
                 rat_x_,
                 rat_y_):
        self.rat_x = rat_x_
        self.rat_y = rat_y_


def trangle_area(rat_point1, rat_point2, rat_point3):
    """
    """
    x1 = rat_point1.rat_x
    y1 = rat_point1.rat_y
    x2 = rat_point2.rat_x
    y2 = rat_point2.rat_y
    x3 = rat_point3.rat_x
    y3 = rat_point3.rat_y

    return 0.5 * ((x1*y2 + x2*y3 + x3*y1 - x1*y3 - x2*y1 - x3*y2).to_num())



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

def test_trangle_area():
    """
    """
    print "[Test trangle area]"
    p1 = RatPoint(RatNum(0, 1), RatNum(0, 1))
    p2 = RatPoint(RatNum(1, 1), RatNum(0, 1))
    p3 = RatPoint(RatNum(0, 1), RatNum(1, 2))
    area = trangle_area(p1, p2, p3)
    print area




if __name__ == "__main__":
    test_ratnum()
    test_trangle_area()
