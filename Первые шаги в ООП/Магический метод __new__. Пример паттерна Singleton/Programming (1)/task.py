# здесь объявляйте класс SingletonFive
class SingletonFive:
    __obj_list = []

    def __new__(cls, *args, **kwargs):
        if len(cls.__obj_list) < 5:
            obj = super().__new__(cls)
            cls.__obj_list.append(obj)
        return cls.__obj_list[-1]

    def __init__(self, name):
        self.name = name


objs = [SingletonFive(str(n)) for n in range(10)]  # эту строчку не менять
