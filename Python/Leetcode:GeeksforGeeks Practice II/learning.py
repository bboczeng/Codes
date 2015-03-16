__author__ = 'bozeng'

def f(x):
    f.count=getattr(f,'count',0)+1

f(1)
f(1)
f(1)
f(1)
f(1)
f(1)
print(f.count)

print(f.__dict__)