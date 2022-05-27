class A:
    value_b = None

    def __init__(self, a):
        self.__a = a
        self.__b = self.value_b

    @property
    def a(self):
        return self.__a

    @property
    def b(self):
        return self.__b


if __name__ == '__main__':
    class_list = []

    class_list.append(A)
    a = A(a=1)
    print(a.a)
    print(a.b)
    print(type(a))
    print("\n")

    class_b = type('B', (A,), {})
    class_list.append(class_b)
    b = class_b(a=2)
    print(b.a)
    print(b.b)
    print(type(b))
    print("\n")

    class_c = type('C', (A,), {'value_b': 3})
    class_list.append(class_c)
    c = class_c(a=4)
    print(c.a)
    print(c.b)
    print(type(c))
    print("\n")

    for class_option in class_list:
        print('Is object "a" of class "%s": %s' % (class_option.__name__, isinstance(a, class_option)))
        print('Is object "b" of class "%s": %s' % (class_option.__name__, isinstance(b, class_option)))
        print('Is object "c" of class "%s": %s' % (class_option.__name__, isinstance(c, class_option)))
        print("\n")
