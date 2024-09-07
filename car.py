import pygame
from pygame import Rect
from random import randint, choice

class Car:
  
  # constructor for Car object
  def __init__(self):
    
    # direction and speed
    self.dy = choice((-2, 2))
    
    # starting position
    if self.dy == 2:
      y = -81
    else:
      y = 400
    
    # rectangle for the car
    spawnrange = randint(200,  500)
    self.rect = Rect(spawnrange, y, 50, 81)

  # called each frame
  def update(self):
    self.rect.y += self.dy

  # draws 
  def draw(self, screen):
    pygame.draw.rect(screen, (250, 0, 0), self.rect)
    
    







# 200 - 500