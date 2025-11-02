class Timer:

    def __init__(self, name_func):
        self.func = name_func

    def __call__(self, *args, **kwargs):
        print("Запущена функция")
        result = self.func(*args, **kwargs)
        print("Функция завершена")
        return result
    

@Timer
def my_func(a: int, b: int) -> int:
    return a + b

