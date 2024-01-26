def decor(func):
    def wrapper():
        print('start')
        func()
        print('end')
    return wrapper
#applying decorator in function

@decor
def printt():
    print('dhruv')

#printt=decor(printt)

printt()