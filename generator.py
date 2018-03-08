def producter():
    res = True
    n = 5
    while n > 0:
        yield res
        n -= 1


def consumer(producter):
    res = yield from producter


if __name__ == '__main__':
    pro = producter()
    con = consumer(pro)
    print(list(con))





