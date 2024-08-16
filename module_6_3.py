class Horse:
    x_distance = 0  # - пройденный путь.
    sound = 'Frrr'

    def __init__(self):
        super().__init__()

    def run(self, dx):
        self.x_distance += dx
        self.x_distance = self.x_distance


class Eagle:  # класс описывающий орла. Объект этого класса обладает следующими атрибутами
    y_distance = 0  # - высота полёта
    sound = 'I train, eat, sleep, and repeat'  # - звук, который издаёт орёл (отсылка)

    def __init__(self):
        super().__init__()

    def fly(self, dy):
        self.y_distance += dy
        self.y_distance = self.y_distance


class Pegasus(Horse, Eagle):  # - класс описывающий пегаса. Наследуется от Horse и Eagle
    def __init__(self):
        super().__init__()

    def move(self, dx, dy):
        self.dx = super().run(dx)
        self.dy = super().fly(dy)

    def get_pos(self):
        return self.x_distance, self.y_distance  # возвращает текущее положение пегаса в виде кортежа

    def voice(self):
        print(Eagle.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
