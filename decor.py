from datetime import datetime


def parametrized_decor(parameter):
    def decor(foo):
        def new_foo(*args, **kwars):
            date_time = datetime.now()
            func_name = foo.__name__
            result = foo(*args, **kwars)
            file_log = parameter+'decoratorlogs.txt'
            with open(file_log, 'a', encoding='utf-8') as file:
                file.write(f'Дата/время: {date_time}\n'
                           f'Имя функции: {func_name}\n'
                           f'Аргументы: {args, kwars}\n'
                           f'Результат: {result}\n')
            return result

        return new_foo

    return decor


@parametrized_decor(parameter='c:\\git\\DEcorator\\1\\')
def foo():
    pass


if __name__ == '__main__':
    foo()