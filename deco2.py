def start_end_decorator(func):

    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args,**kwargs)
        print ('end')
        return result
    return wrapper

@start_end_decorator
def add5(x):
    return x + 5

result = add5(10)
print(result)