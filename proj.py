from pygame import *

width = 700 
height = 500 
window = display.set_mode((width, height)) 
display.set_caption('123')

class GameSprite(sprite.Sprite):
    def init(self, player_image, player_x, player_y, size_x, size_y, player_speed): 
        sprite.Sprite.init(self)

    self.image = transform.scale(image.load(player_image), (size_x, size_y))
    self.speed = player_speed
    self.rect = self.image.get_rect()
    self.rect.x = player_x
    self.rect.y = player_y
def reset(self):
    window.blit(self.image, (self.rect.x, self.rect.y))


x = 10
y = 10


class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT]:
             x -= 10
        if keys_pressed[K_RIGHT]:
             x += 10




finish = False

game = True

speed_x = 3 
speed_y = 2

while game: 
    ball.rect.x += speed_x 
    ball.rect.y += speed_y

for e in event.get():
    if e.type == QUIT:
        game = False
display.update()