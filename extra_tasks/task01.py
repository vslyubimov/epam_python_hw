'''
1) Написать декоратор, который применяется к любой функции,
в зависимости от возвращаемого типа результата
декорируемой функции записывает этот результат в файл с именем вида:
{тип_результата}.txt, файл не должен перетираться,
также я могу посмотреть оригинальную информацию (например докстринг)
декорируемой функции
пример:

@custom_deforator
def some_func(params: list):
    return sum(params)

@custom_decorator
def another_func(params: list):
    """DOCSTRING """
    return "\n".join(params)

print(another_func.__doc__) #    """DOCSTRING """

OUTPUT: 2 файла в каждом есть запись от одной из функций
(т.е. все целочисленые результаты хранятся в файле с именем,
например integer.txt)
Если функция возвращает какой-то инстанс класса, записывать
его аттрибуты в файл json формата, в виде
"class_instance_name" : {attr1: value, ...}
'''

import json
import os.path
from functools import wraps


def custom_decorator(func):
    @wraps(func)
    def wrapper(*args):
        func_result = func(*args)
        if hasattr(func_result, '__dict__'):

            if not os.path.exists('class_attrs.json'):
                with open('class_attrs.json', 'w') as js:
                    execute_data = {}
                    json.dump(execute_data, js)

            else:
                with open('class_attrs.json') as js:
                    data = json.load(js)
                    data[func_result.__class__.__name__] = func_result.__dict__

                with open('class_attrs.json', 'w') as js:
                    print(data)
                    json.dump(data, js)

        else:
            res_type = type(func_result).__name__
            with open(f'{res_type}.txt', 'a') as file:
                file.write(f'{str(func_result)}\r\n')
        return func_result

    return wrapper


@custom_decorator
def some_func(params: list):
    return sum(params)


@custom_decorator
def another_func(params: list):
    """DOCSTRING """
    return "\n".join(params)


@custom_decorator
def json_func(params):
    class A:
        def __init__(self, arg):
            self.arg = arg

    return A(params)


print(another_func.__doc__)  # """DOCSTRING """
some_func([1, 2, 3])
another_func('123')
json_func([1, 2, 3])
print(another_func.__name__)


class A:
    def __init__(self, a):
        self.a = a
