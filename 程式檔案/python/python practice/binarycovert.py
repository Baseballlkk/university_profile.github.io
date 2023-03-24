
def binaryconvert():
    x = input('input a number:')
    x = int(x)
    a = x%2
    b = ((x-a)/2)%2
    c = ((((x-a)/2)-b)/2)%2
    d = ((((((x-a)/2)-b)/2)-c)/2)%2
    e = ((((((((x-a)/2)-b)/2)-c)/2)-d)/2)%2
    f = ((((((((((x-a)/2)-b)/2)-c)/2)-d)/2)-e)/2)%2
    g = ((((((((((((x-a)/2)-b)/2)-c)/2)-d)/2)-e)/2)-f)/2)%2
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    e = int(e)
    f = int(f)
    g = int(g)
    print(g,'',f,'',e,'',d,'',c,'',b,'',a)

for i in range(2):
    k,l,m,n,o,p = binaryconvert()
    k = int(k)
    l = int(l)
    m = int(m)
    n = int(n)
    o = int(o)
    p = int(p)

    A = [k,l,m,n,o,p]
    for j in range(6):
        print(j)
