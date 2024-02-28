class Ball:
    def __init__(self, color, size):
        self.color = color
        self.size = size

    def direction(self, direction):
        if direction.lower() in ['вверх','вверх в лево','вверх в право','вниз','вниз в лево','вниз в право','налево','направо']:
            print(f' {color} {size} мяч движется {direction.lower()}')
        else:
            print('Неверное направление')

color = input('Введите цвет мяча: ')
size = input('Введите размер мяча: ')
direction_input = input('Выберите направление движения (вверх, вверх в лево, ввверх в право, вниз, вниз в лево, вниз в право, налево, направо): ')

my_ball = Ball(color, size)

my_ball.direction(direction_input)
