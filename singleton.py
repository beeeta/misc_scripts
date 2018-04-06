"""
python 单例模式的几种方法

"""
from functools import wraps


# 使用 __new__ 实现
class Single1:
    __instance = {}
    def __new__(cls, *args, **kwargs):
        if cls not in cls.__instance:
            print('-----------create instance')
            cls.__instance[cls] = super(Single1,cls).__new__(cls,*args,**kwargs)
        else:
            print('----------instance existed')
        return cls.__instance[cls]


# 使用装饰器
def single(cls):
    _instance = {}

    @wraps(cls)
    def inner(*args,**kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args,**kwargs)
        return _instance[cls]
    return inner


@single
class Single2:
    pass


# 使用元类

class SingMate(type):
    __instance = {}
    def __call__(cls, *args, **kwargs):
        if cls not in SingMate.__instance:
            print('-------create---------------')
            print(cls)
            SingMate.__instance[cls] = type.__call__(cls,*args,**kwargs)
        print('----------created-------------')
        return SingMate.__instance[cls]

class Single3(metaclass=SingMate):
    pass

# 使用模块的单例性,在其他模块中引入
class Single4:
    pass

single4 = Single4()