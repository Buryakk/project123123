from pygame import *

width = 700 
height = 500 
window = display.set_mode((width, height)) 
display.set_caption('123')

bf = transform.scale(image.load('bf.jpg'), (700, 500))
r1 = transform.scale(image.load('rr1.png'), (170, 30))

x = 290
y = 10
x3 = 290
y3 = 490
x2 = 0
y2 = 0

class Player():
    def update(self):
        keys_pressed = key.get_pressed(r1)
        if keys_pressed[K_LEFT]:
             x -= 10
        if keys_pressed[K_RIGHT]:
             x += 10
finish = False

game = True

speed_x = 3 
speed_y = 2

while game:
    window.blit(bf, (x2, y2))
    window.blit(r1, (x, y))
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
time.delay(100)