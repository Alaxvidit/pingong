from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self,sp_speed,sp_x,sp_y,width,height,sp_image=None):
        super().__init__()
        if sp_image == None:
            self.image = Surface((width,height))
            self.image.fill((0,0,0))
        else:
            self.image = transform.scale(image.load(sp_image),(width,height))
        self.speed = sp_speed

        self.rect = self.image.get_rect()
        self.rect.x = sp_x
        self.rect.y = sp_y
    
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Rocket(GameSprite):
    def __init__(self,sp_speed,sp_x,sp_y,width,height,color,):
        super().__init__(sp_speed,sp_x,sp_y,width,height)
        self.fill_color = color
        self.image.fill(color)

    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_h - 80:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_h - 80:
            self.rect.y += self.speed

# палитра
rocket1_color = (0,0,255)
rocket2_color = (255,0,0)
back = (200,255,255)
# создание фона и окна
win_w = 600
win_h = 500
window = display.set_mode((win_w,win_h))
display.set_caption('ping-pong')
window.fill(back)
# создание ракеток и мяча
rocket1 = Rocket(10,0,0,10,125,rocket1_color)
rocket2 = Rocket(10,win_w-10,0,10,125,rocket2_color)
ball = GameSprite(4,200,200,50,50,'ball.png')

game = True
finish = False
clock = time.Clock()
FPS = 60


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        rocket1.update_l()
        rocket2.update_r()
        ball.rect.x += ball.speed
        ball.rect.y += ball.speed

        rocket1.reset()
        rocket2.reset()
        ball.reset()
        
    display.update()
    time.delay(50)
