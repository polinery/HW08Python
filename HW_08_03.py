''' 3. Создайте собственный класс-исключение, обрабатывающий ситуацию деления
на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно
обработать эту ситуацию и не завершиться с ошибкой. '''


class DivisionByNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    def divide_by_null(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Деление на ноль недопустимо")


print(DivisionByNull.divide_by_null(int(input('Делимое: ')),
                                    int(input('Делитель: '))))
