from time import sleep, time

# 统计一个函数执行时间的装饰器
def total_time(fun):
    def f():
        before = time()
        fun()
        after = time()
        print(after-before)
    return f


@total_time
def play():

    sleep(4)

    print("LOL真好玩，小学生都被你坑得撕心裂肺了")


@total_time
def run():

    sleep(3)

    print("我喜欢跑步")


def dynamic_change(num):
    def change(fun):
        def f(*args , **kwargs):
            if num > 5:
                fun(*args, **kwargs)
            else:
                print("这个辣椒真难吃，免费送")
        return f
    return change


@dynamic_change(10)
def price():

    print("这个辣椒五块钱一个")


if __name__ == '__main__':
    # before = time()
    # play()
    # after = time()
    # print(after-before)
    #
    # before = time()
    # run()
    # after = time()
    # print(after - before)

    # play()
    #
    # run()

    price()

