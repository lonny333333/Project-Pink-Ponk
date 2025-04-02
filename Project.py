from pygame import *

window = display.set_mode((700,500))
fon = (0, 255, 149)
window.fill(fon)
clock = time.Clock()
fps = 60

class GameSprite (sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_with, player_hight):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_with,player_hight))
        self.rect = self.image.get_rect()
        self.rect.y = player_y
        self.rect.x = player_x
        self.speed = player_speed
    def resset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Plaer (GameSprite):
    def update_L(self):
        key_pressed = key.get_pressed()
        if key_pressed [K_s] and self.rect.y <395:
            self.rect.y += self.speed
        if key_pressed [K_w] and self.rect.y >5:
            self.rect.y -= self.speed
    def update_R(self):
        key_pressed = key.get_pressed()
        if key_pressed [K_DOWN] and self.rect.y <395:
            self.rect.y += self.speed
        if key_pressed [K_UP] and self.rect.y >5:
            self.rect.y -= self.speed
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > 500:
            self.rect.y = 0
            self.rect.x = randint(50,650)
            lost += 1

rocket1 = Plaer('pngwing.com.png', 20,70 , 2 , 50, 100)
rocket2 = Plaer('pngwing.com.png', 630,70 , 2 , 50, 100)
boll = Enemy('pngwing.com (1).png', 350,250, 2 , 50 ,50)

game = True
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
    window.fill(fon)
    rocket1.update_L()
    rocket1.resset()
    rocket2.update_R()
    rocket2.resset()
    #boll.update()
    boll.resset()

    display.update()
    clock.tick(fps)