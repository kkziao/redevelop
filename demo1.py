import math


def judge(n):   # 输入一个大于1的整数,是质数返回True，否则返回false
    if n % 1 != 0:
        raise ValueError
    else:
        if n == 1:
            return True
        else:
            sqr = n ** 0.5      # 之后要用到平方根
            if sqr % 1 == 0:    # 平方根是整数吗？
                # print("sqr of {0} is int.".format(n))
                return False
            sqr = math.ceil(sqr)   # 向上取整
            # print("ceil(sqr) of {0} is {1}.".format(n, sqr))
            for i in range(2, sqr):  # 暴力验证
                # print("fuck!{0} is not the factor of {1}.".format(i, n))
                if n % i == 0:
                    return False
            return True


# test--100以内26个质数，1000以内169个质数，10000以内9592个，包括1
scope = 100
scope = scope + 1
li = []
for r in range(1, scope):
    if judge(r):
        li.append(r)
print(len(li))

