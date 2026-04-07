from functools import wraps


def decor1(func):
    @wraps(func)
    def wrapper(x):
        '''hello here'''
        return func(x)
    
    return wrapper


def decor2(func):
    def wrapper(x):
        '''hamza hindi'''
        return func(x)
    
    return wrapper

@decor1
def func1(x):
    print(x)

@decor2
def func2(x):
    print(x)
    
print(func1.__doc__)
print(func2.__doc__)