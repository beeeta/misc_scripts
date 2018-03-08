def test_send():
    print('test_send:before n=10') # 3
    n = 10
    while n>0:
        print('test_send:while:{}'.format(n)) # 4 8
        result = yield n
        print('test_send:while:{} after yield'.format(n)) # 6
        print('get a result:{}'.format(result)) # 7
        n -= 1

if __name__ == '__main__':
    print('before tset_send') # 1
    ts = test_send()
    print('before send none') # 2
    ts.send(None)
    print('before send 1111') # 5
    res = ts.send(1111)
    print('after send 1111,res:{}'.format(res))
