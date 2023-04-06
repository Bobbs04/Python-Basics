def decorator_func(original):
    def wrapper_func():
        print("Winnie")
        return original()
    return wrapper_func


def message():
    print('Hello Winnie')


decorated_func = decorator_func(message)
decorated_func()


def decorator_func(original):
    def wrapper_func(*args, **kwargs):
        print(f'Wrapper executed this before {original.__name__}')
        return original(*args, **kwargs)
    return wrapper_func


@decorator_func
def message():
    print('Hello Winnie')


@decorator_func
def display_info(name, age):
    print(f'Display_info ran with arguments {name}, {age}')


display_info('John', 'age')
message()


def display_info(func):
    def inner():
        print(f'Executing {func.__name__} function')
        func()
        print("Finished Executing")

    return inner


@display_info
def printer():
    print("Hello world")


printer()
printers = display_info(printer)
printers()


def smart(func):
    def inner(a, b):
        print(f'Dividing {a / b}')
        if a == 0:
            print("Can't divide by 0")
        else:
            print("Divisible")

        return func(a, b)
    return inner


@smart
def divide(a, b):


divide(10, 2)