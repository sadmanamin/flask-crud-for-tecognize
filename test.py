def a(b):
    print(1)
    def inner():
        print(2)
        b()
        print(3)
    return inner

@a
def b():
    print('Inside b')

b()