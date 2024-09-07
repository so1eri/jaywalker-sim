import pygame
from pygame import Rect
from random import randint, choice

class Truck:

  # constructor for Truck object
  def __init__(self):

    # direction and speed
    self.dy = choice((-3, 3))

    # starting position
    if self.dy == 2:
      y = -88
    else:
      y = 400

    # rectangle for the car
    spawnrange = randint(200,  500)
    self.rect = Rect(spawnrange, y, 54, 88)

  # called each frame
  def update(self):
    self.rect.y += self.dy

  # draws 
  def draw(self, screen):
    pygame.draw.rect(screen, (128, 128, 128), self.rect)