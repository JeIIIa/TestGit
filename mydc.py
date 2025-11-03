class Timer:

    def __init__(self, name_func: function):
        self.func = name_func

    def __call__(self, *args, **kwargs):
        print("Запущена функция")
        result = self.func(*args, **kwargs)
        print("Функция завершена")
        return result
    

@Timer
def my_func(a: int, b: int) -> int:
    return a + b

@Timer
def my_func_two(a: int | float, b: int | float, c: float | int) -> float | int:
    return a + b + c
