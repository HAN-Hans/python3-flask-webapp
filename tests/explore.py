from functools import wraps


def a(f):
    @wraps(f)
    def d(*args, **kwargs):
        print("before")
        f(*args, **kwargs)
        print("after")
    print(f.__name__)
    return d


@a  # p = a(p)
def p():
    print(__name__)
p()
print(p.__name__)


print()

def b(name):
    def a(f):
        # @wraps(f)
        def d(*args, **kwargs):
            print("before")
            f(*args, **kwargs)
            print('call %s():' % f.__name__)
            print("after")
        print(f.__name__)
        return d
    print(name)
    return a

# p()  ->  b(name)()(f)
@b('han')
def p():
    print(__name__)
p()
print(p.__name__)

