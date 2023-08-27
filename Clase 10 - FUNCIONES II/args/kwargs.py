def suma(*args):
    return sum(args)

print(suma(10,20,30))


def suma(**kwargs):
    print(kwargs)
    return sum(kwargs.values())

print(suma(a=10,b=20,c=30))