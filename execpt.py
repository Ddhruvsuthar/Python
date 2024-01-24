try:
    a= 5/0
    b= a + 10
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print('everything is fine')
finally:
    print('running')