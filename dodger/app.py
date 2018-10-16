import os
import pygame
from dodger import Dodger


class App:
    def __init__(self):
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        self.__width = 500
        self.__height = 500
        self.__name = "Dodger"

    def start(self):
        pygame.init()
        pygame.display.set_caption(self.__name)
        self.__window = pygame.display.set_mode((500, 500))

        dodger = Dodger("Cy")

        run = True
        while run:
            pygame.time.delay(50)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                dodger.move_left()
            if keys[pygame.K_RIGHT]:
                dodger.move_right()

            self.__window.fill((0, 0, 0))
            d_info = dodger.get_info()
            pygame.draw.circle(
                self.__window,
                (255, 0, 0),
                (d_info["x"], d_info["y"]),
                d_info["radius"],
            )
            pygame.display.update()

        pygame.quit()


if __name__ == "__main__":
    app = App()
    app.start()
