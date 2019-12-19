
def f(*args, **kwargs):
    print(args, kwargs)

def f2(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)

def f3(arg1, *args, arg2, **kwargs):
    print(arg1, args, arg2, kwargs)

if __name__ == "__main__":
    l = [1,2,3]
    t = (4,5,6)
    d = {'a':7, 'b':8, 'c':9}
    print("=======")
    f()
    f(1,2,3)
    f(1,2,3,"groovy")
    f(a=1,b=2,c=3)
    f(a=1,b=2,c=3,zzz="hi")
    f(1,2,3,a=1,b=2,c=3)
    f(*l, **d)
    f(*t, **d)
    f(1,2,*t)
    f(q="winning",**d)

    print("=======")
    f2(1, 3, 2)
    f2(1, 2, 3, "groovy")
    f2(arg1=1, arg2=2, c=3)
    f2(arg1=1, arg2=2, c=3, zzz="hi")
    f2(1, 2, 3, a=1, b=2, c=3)
    f2(*l, **d)
    f2(*t, **d)
    f2(1, 2, *t)
    f2(1,1,q="winning",**d)
    f2(1,2,*t,q="winning",**d)

    print("=======")
    f3(arg1=1, arg2=2, c=3, zzz="hi")
    f2(1, 2, c=3, zzz="hi")
    f3(1, 2, c=3, zzz="hi")



