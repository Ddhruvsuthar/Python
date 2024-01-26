def fib(limit):
    a,b=0,1
    while a < limit:
        yield a 
        a,b = b, a + b

fibb = fib(10)
for i in fibb:
    print(i)