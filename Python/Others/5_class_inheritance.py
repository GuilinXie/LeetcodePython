class A(object):
    def go(self):
        print("go A go!")
    def stop(self):
        print("stop A stop!")
    def pause(self):
        raise Exception("Not Implemented")
class AA(object):
    def go(self):
        print("go AA go!")
    def stop(self):
        print("stop AA stop!")
    def pause(self):
        raise Exception("Not Implemented")

class M(AA):
    def go(self):
        super(M, self).go()
        print("go M go!")
    def stop(self):
        print("stop M stop!")
    def pause(self):
        raise Exception("Not Implemented")

class B(A):
    def go(self):
        super(B, self).go()
        print("go B go!")

class C(AA):
    def go(self):
        super(C, self).go()
        print("go C go!")
    def stop(self):
        super(C, self).stop()
        print("stop C stop!")

class D(M,B,C):
    def go(self):
        super(D, self).go()
        print("go D go!")
    def stop(self):
        super(D, self).stop()
        print("stop D stop!")
    def pause(self):
        print("wait D wait!")

class E(B,C): pass

if __name__ == "__main__":
    a = A()
    b = B()
    c = C()
    d = D()
    e = E()
    print ("1 =====")
    print ("a.go()")
    a.go()
    print("------")
    print("b.go()")
    b.go()
    print("------")
    print("c.go()")
    c.go()
    print("------")
    print("d.go()")
    d.go()
    print("------")
    print("e.go()")
    e.go()
    print ("2 =====")
    print("a.stop()")
    a.stop()
    print("------")
    print("b.stop()")
    b.stop()
    print("------")
    print("c.stop()")
    c.stop()
    print("------")
    print("d.stop()")
    d.stop()
    print("------")
    print("e.stop()")
    e.stop()
    print ("3 =====")
    print("a.pause()")
    a.pause()
    print("------")
    print("b.pause()")
    b.pause()
    print("------")
    print("c.pause()")
    c.pause()
    print("------")
    print("d.pause()")
    d.pause()
    print("------")
    print("e.pause()")
    e.pause()