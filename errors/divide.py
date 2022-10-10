
def divide(a, b):
    try:
        result = a/b
    except (ZeroDivisionError, TypeError) as err:
        print('Dividing by 0 will not work and you must use numbers!!')
        print(err)
    else:
        print(f'{a} divided by {b} = {result}')


print(divide(5, 2))
