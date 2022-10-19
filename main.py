class Parallelepiped:
    a = 1
    b = 1
    c = 1

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __del__(self):
        print('Вызван деструктор,объект удален')

    def getA(self):
        return self.a

    def getB(self):
        return self.b

    def getC(self):
        return self.c

    # Метод расчета площади.
    def getArea(self):
        return 2 * (self.a * self.b + self.b * self.c + self.a * self.c)

    # Метод расчета объема.
    def getVolume(self):
        return self.a * self.b * self.c

    def getInfo(self):
        print('Сторона A:' + str(self.a) + '\n' + 'Сторона B:' + str(self.b) + '\n' + 'Сторона С:' + str(
            self.c) + '\n' + 'Площадь :' + str(self.getArea()) + '\n' + 'Объем :' + str(self.getVolume()))
        print('--------------------------------------------------------------------')


while True:
    try:
        print('Введите сторону А первого параллелепипеда  :')
        a = int(input())
        if a < 1:
            raise Exception
        print('Введите сторону В первого параллелепипеда  :')
        b = int(input())
        if b < 1:
            raise Exception
        print('Введите сторону С первого параллелепипеда  :')
        c = int(input())
        if c < 1:
            raise Exception
        p1 = Parallelepiped(a, b, c)
        p2 = Parallelepiped(2, 5, 10)
        p3 = Parallelepiped(10, 10, 10)
        break
    except ValueError:
        print('Некорректное число')
    except Exception:
        print('Введите число,большее 0:')

p1.getInfo()
p2.getInfo()
p3.getInfo()
