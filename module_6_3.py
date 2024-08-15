class Horse:
    def __init__(self):
        super().__init__()
        print('init Horse')

    x_distance = 0  # - пройденный путь.
    sound = 'Frrr'
    def run(self, dx):
        self.x_distance += dx
        self.x_distance = self.x_distance


class Eagle:  #  класс описывающий орла. Объект этого класса обладает следующими атрибутами

    def __init__(self):
        print('init eagle')
    y_distance = 0   #  - высота полёта

    def fly(self, dy):
        self.y_distance += dy
        self.y_distance = self.y_distance


    sound = 'I train, eat, sleep, and repeat'   # - звук, который издаёт орёл (отсылка)



class Pegasus(Horse, Eagle):    #  - класс описывающий пегаса. Наследуется от Horse и Eagle
    def move(self, dx, dy):
        self.dx = super().run(dx)
        self.dy = super().fly(dy)


    def get_pos(self):
        return self.x_distance, self.y_distance # возвращает текущее положение пегаса в виде кортежа

    def voice(self):
        print(Eagle.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()