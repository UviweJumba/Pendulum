import pygame, sys
from pygame.locals import *
from physics import Pendulum, RK4_Pendulum


class App:

    def __init__(self):
        pygame.init()

        self.FPS = 120
        self.clock = pygame.time.Clock()
        self.WIN_DIM = [1080, 600]
        self.screen = pygame.display.set_mode(self.WIN_DIM)

        self.pendulum = RK4_Pendulum(self.screen, self.WIN_DIM)

    def run(self):

        while True:
            t = pygame.time.get_ticks()/1000 ## Elapsed time in seconds
            dt = self.clock.get_time()/1000  ## Delta time (time since last call) in seconds

            self.screen.fill((50, 50, 50))

            for evnt in pygame.event.get():

                if evnt.type == QUIT:
                    pygame.quit()
                    sys.exit()

            self.pendulum.update(t, dt)

            pygame.display.update()
            self.clock.tick(self.FPS)

def main():
    app = App()
    app.run()

if __name__ == "__main__":
    main()