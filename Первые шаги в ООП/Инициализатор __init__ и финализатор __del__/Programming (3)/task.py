# здесь объявите класс TriangleChecker
class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        a, b, c = self.a, self.b, self.c
        if not all(map(lambda x: type(x) in (int, float), (a, b, c))):
            return 1

        if not all(map(lambda x: x > 0, (a, b, c))):
            return 1

        if a >= b + c or b >= a + c or c >= a + b:
            return 2
        return 3


a, b, c = map(int, input().split())  # эту строчку не менять
# здесь создайте экземпляр tr класса TriangleChecker и вызовите метод is_triangle() с выводом информации на экран
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())
