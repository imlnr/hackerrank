class P:
    def fu1(self):
        print('this is a parent function')


class C(P):
    def fu2(self):
        print('this is a child function')

class D(C):
    def fu3(self):
        print('this is grandchild')

ob = D()
ob.fu1()
ob.fu2()
ob.fu3()