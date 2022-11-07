
# * MRO: Method Resolution Order
# ? Whenever you create a class, Python sets a METHOD RESOLUTION ORDER, or MRO
# ? Which is the order in which Python will look for methods on instances of that class

# * How to access MRO
# ? __mro__ attribute
# ? mro() method on the class
# ? Builtin help(cls) method


class A:
    def do_something(self):
        print("Method defined in: A")


class B(A):
    def do_something(self):
        print("Method defined in: B")


class C(A):
    def do_something(self):
        print("Method defined in: C")


class D(B, C):
    def do_something(self):
        print("Method defined in: D")


thing = D()
thing.do_something()

print(D.__mro__)
