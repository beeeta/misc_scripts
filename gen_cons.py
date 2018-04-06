# 用协程实现一个生产者消费者模式

def producters():
    pros = None
    while True:
        yl = yield  pros
        pros = 'apple:' + str(yl)

def consumer(producters):
    producters.send(None)
    n = 5
    while n>0:
        yield producters.send(n)
        n -= 1

if __name__ == '__main__':
    pro = producters()
    print(list(consumer(pro)))


