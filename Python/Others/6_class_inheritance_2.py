class A:
    def say(self):
        print("A Saying:", self)

class AA:
    def say(self):
        print("AA Saying:", self)

class B(A):
    def eat(self):
        print("B Eating:", self)
    def say(self):
        super().say()
        print ("B Saying:")
class C(AA):
    def eat(self):
        print("C Eating:", self)
    def say(self):
        super(C, self).say()
        print ("C Saying:")
class D(B, C):
    def say(self):
#        super(D, self).say()
        print("D Saying:", self)
    def dinner(self):
        self.say()
        super().say()
        self.eat()
        super().eat()
        C.eat(self)
if __name__ == "__main__":
    d = D()
    # d.eat()
    # C.eat(d)
    d.say()

'''
class D(B, C):  for say()  function, when D.say() has super()
case 1: 
->if B,C inherit the same A

--> if B has super(), and C doesn't have super().
---> output: C, B, D

--> if B has super(), and C has super() too.
---> output: A, C, B, D

--> if B doesn't have super(), and C has super().
---> output: B, D

--> if B doesn't have super(), and C doesn't have super().
---> output: B, D

case2:
if B, C inherit different A, AA

--> if B has super(), and C doesn't have super().
---> output: A, B, D

--> if B has super(), and C has super() too.
---> output: A, B, D

--> if B doesn't have super(), and C has super().
---> output: B, D

--> if B doesn't have super(), and C doesn't have super().
---> output: B, D

--> if D.eat() doesn't have super() at all
---> output: D
 
'''