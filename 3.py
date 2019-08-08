def wrap1(f):
    def decorator(*args, **kw):
        print ('Call %s() in wrap1' % f.__name__)
        return f(*args, **kw)
    return decorator


def wrap2(f):
    def decorator(*args, **kw):
        print ('Call %s() in wrap2' % f.__name__)
        return f(*args, **kw)
    return decorator


@wrap2
@wrap1
def func(a, b):
    return a * 10 + b


if __name__ == '__main__':
    print(func(5, 6))
    a = 1
    print(a)
