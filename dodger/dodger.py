class Dodger:
    def __init__(self, name):
        self.name = name
        self.__radius = 25
        self.score = 0
        self.life = 3
        self.__x = 250
        self.__y = 450
        self.__velocity = 5

    def move_left(self):
        self.__x -= self.__velocity

    def move_right(self):
        self.__x += self.__velocity

    def get_info(self):
        return dict(x=self.__x, y=self.__y, radius=self.__radius)
