import pygame
from pygame import Rect
from random import randint, choice

class Motorcycle:

  # constructor for Motorcycle object
  def __init__(self):

    # direction and speed
    self.dy = choice((-4, 4))

    # starting position
    if self.dy == 2:
      y = -63
    else:
      y = 400

    # rectangle for the car
    spawnrange = randint(200,  500)
    self.rect = Rect(spawnrange, y, 38,63)

  # called each frame
  def update(self):
    self.rect.y += self.dy

  # draws 
  def draw(self, screen):
    pygame.draw.rect(screen, (0, 0, 0), self.rect)