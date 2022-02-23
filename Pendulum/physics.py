import pygame
from pygame import Vector2
import math
import cv2
import numpy as np

GRAVITY = 9.8

class Pendulum:

    def __init__(self, screen, win_size= []):
        self.screen = screen
        self.WIN_SIZE = win_size

        self.scale = 20     ## Scales the length of the rod to make it look appropriate

        self.mass = 1
        self.length = 10

        self.mu = 0.2

        self.theta = math.pi/4
        self.theta_d = 0
        self.theta_dd = 0

        self.origin = Vector2(self.WIN_SIZE[0]/2, self.WIN_SIZE[1]/2)
        self.position = Vector2(0, 0)


    def update(self , t, dt):
        ## Theta_dd = -mu * theta_d - (mg/length) * sin(theta)

        self.theta_dd = -self.mu * self.theta_d - (self.mass*GRAVITY/self.length) * math.sin(self.theta)

        self.theta_d += self.theta_dd * dt

        self.theta += self.theta_d * dt

        print("Theta: ", self.theta)




        self.position = Vector2(self.length*math.sin(self.theta)*self.scale, self.length*math.cos(self.theta)*self.scale).__add__(self.origin)

        pygame.draw.line(self.screen, (255, 255, 255), self.origin, self.position)
        #pygame.draw.circle(self.screen, (0, 255, 0), self.origin, 2)
        pygame.draw.circle(self.screen, (255, 0, 0), self.position, 5)


class RK4_Pendulum:

    def __init__(self, screen, win_size= []):
        self.screen = screen
        self.WIN_SIZE = win_size

        self.scale = 20

        self.mass = 1
        self.length = 10

        self.mu = 0

        ## INITAL STATE
        self.y = np.array([np.pi/4, 0])        ## Theta, Theta_d

        self.origin = Vector2(self.WIN_SIZE[0] / 2, self.WIN_SIZE[1] / 2)
        self.position = Vector2(0, 0)

    def y_dot(self, y):
        return np.array([self.y[1], -self.mu * self.y[1] -(GRAVITY/self.length)*np.sin(self.y[0])])

    def step(self, y, dt):
        k1 = self.y_dot(y)
        k2 = self.y_dot(y + k1*0.5*dt)
        k3 = self.y_dot(y + k2*0.5*dt)
        k4 = self.y_dot(y + k3*dt)

        return dt*(k1 + 2*k2 + 2*k3 + k4)/6

    def update(self, t, dt):
        self.y = self.y + self.step(self.y, dt)

        self.position = Vector2(self.length * math.sin(self.y[0]) * self.scale,
                                self.length * math.cos(self.y[0]) * self.scale).__add__(self.origin)

        pygame.draw.line(self.screen, (255, 255, 255), self.origin, self.position)
        # pygame.draw.circle(self.screen, (0, 255, 0), self.origin, 2)
        pygame.draw.circle(self.screen, (255, 0, 0), self.position, 5)

