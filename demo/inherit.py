class D(object):
    # def __init__(self):
    #     print("D init")
    pass

class E(object):
    # def __init__(self):
    #     print("E init")
    pass

class F(object):
    def __init__(self):
        print("F init")
    pass

class C(D, F):
    # def __init__(self):
    #     print("C init")
    pass

class B(E, D):
    # def __init__(self):
    #     print("B init")
    pass

class A(B, C):
    def __init__(self):
        # super(A, self).__init__()
        print("A init")
    pass
ob = A()