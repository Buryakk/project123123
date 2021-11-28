#project123123
from pygame import * 

in_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('123')




class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)


        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

finish = False 

game = True

speed_x = 3
speed_y = 2

while game:
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        
        
        
        
    for e in event.get():
        if e.type == QUIT:
            game = False
       
                
display.update()







