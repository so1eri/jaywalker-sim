from os import environ
from random import choice
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame
from pygame.locals import *
from sys import exit
from pygame import Rect
from car import Car
from truck import Truck
from motorcycle import Motorcycle

# Game settings
pygame.init()
FPS = 30
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("jaywalking sim")
clock = pygame.time.Clock()
Player = Rect(10, 255, 15, 15)
vehicles = []
count = 0
pygame.time.set_timer(USEREVENT, 480) # event to spawn trucks/motorcycles
pygame.time.set_timer(1 ,800) # event to spawn cars
  
# Game loop
def main():
  while True:
    handle_events()
    update()
    draw()

# Event Handling 
def handle_events():
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      exit()
    if 1 == event.type:
      vehicles.append(Car())
    if USEREVENT == event.type:
      options = (Truck(), Motorcycle())
      chosen = choice(options)
      vehicles.append(chosen)
  
      
  # PLayer movement
  keys = pygame.key.get_pressed()
  if keys [K_w]:
    Player.y -= 5
    Player.y = max(1, Player.y) 
  if keys [K_a]:
     Player.x -= 5
     Player.x = max(1, Player.x)
  if keys [K_s]:
    Player.y += 5
    Player.y = min(384, Player.y) 
  if keys [K_d]:
    Player.x += 5
    Player.x = min(585, Player.x)
    # winning
    if Player.x == 585:
      quit_event = pygame.event.Event(QUIT)
      pygame.event.post(quit_event)

# frame by frame logic
def update():
  clock.tick(FPS)
  # remove vehicles
  for vehicle in vehicles:
    vehicle.update()
    if vehicle.rect.y not in range (-81, 401):
      vehicles.remove(vehicle)
  # collision detection
  for vehicle in vehicles:
     collision = Player.collidelist([vehicle.rect])
     if collision != -1:
        Player.x = 10
        global count
        count += 1
       
# display text
def draw():
  screen.fill((0,255,0))
  pygame.draw.rect(screen, (0,240,0), (100,0,600,600))

  # font settings
  font = pygame.font.Font('freesansbold.ttf', 32)
  text = font.render("Deaths " + str(count), True, (0, 0, 0), (0, 255, 0))
  textRect = text.get_rect()
  textRect.x, textRect.y = 0, 0
  screen.blit(text, textRect)

  # draw object to screen
  for vehicle in vehicles:
    vehicle.draw(screen)
  pygame.draw.rect(screen, (0,0,250), Player)
  
  # update display
  pygame.display.flip()

main() # run game