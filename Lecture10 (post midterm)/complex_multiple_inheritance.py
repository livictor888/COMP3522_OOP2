class A:
    pass


class B:
    pass


class C(A):
    pass


class D(A):
    pass


class E(A, B):
    pass


class F(C,D):
    pass


class G(D, E, B):
    pass


class H(F,G):
    pass


print(H.mro())
