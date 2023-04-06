def square(x):
    return x * x


def cube(x):
    return x * x * x


def my_map(func, list_1):
    result = []
    for i in list_1:
        result.append(func(i))
    return result


squares = my_map(cube, [1, 2, 3, 4, 5])
print(squares)


def logger(msg):

    def log_message():
        print(f'Log: {msg}')

    return log_message


log_hi = logger('Hi!')
log_hi()


def html_tag(tag):
    def wrap_text(msg):
        print(f'<{tag}>{msg}</{tag}>')
    return wrap_text


h1 = html_tag('h1')
h1('Test Headline')
h1('Another Headline')


def greeting(msg):
    def person(name):
        print(f'{msg} {name}')
    return person


greet = greeting('Hello')
greet('Winnie')


def add(num):
    def numbers(x):
        print(num + x)
    return numbers


num = add(10)
num(15)


def outer_func(msg):

    def inner():
        print(f'{msg} Elijah')

    return inner


greeting = outer_func('Hey')
greeting()


def cube(x):

    def square():
        print(x * x * x)

    return square


squares = cube(2)
squares()
