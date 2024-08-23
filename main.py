from pygame import *
from random import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w, h):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w, h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.w = w
        self.h = h

    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed

miss = 0
score = 0

class Enemy(GameSprite):
    def update(self):
        if self.rect.y < 650:
            self.rect.y += self.speed

        global miss

        if self.rect.y >= 650:
            miss += 1
            self.rect.x = randint(80, 1120)
            self.rect.y = randint(-100, -50)

mw = display.set_mode((800, 500))
display.set_caption('Ping-Pong')

bg = transform.scale(image.load('table.jpeg'), (800, 500))
player = Player('pingpong.png', 10, 200, 1, 80, 100)

#mixer.init()
#mixer.music.load('?')
#mixer.music.play(-1)

#pong = mixer.Sound('?')

#finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    mw.blit(bg, (0, 0))

    player.reset()
    player.update()

    #for i in monsters:
        #i.reset()
        #i.update()
            
    #for i in Bullets:
        #i.reset()
        #i.update()

    #kill = sprite.groupcollide(Bullets, monsters, True, True)
    #for i in kill:
        #score += 1
        #monster = Enemy('TIE.com.png', randint(80, 1120), randint(-100, -50), randint(1, 5), 80, 100)
        #monsters.add(monster)

    #if miss >= 10:
        #finish = True
        #best = ''
        #with open('reiting.txt', 'w') as file:
            #if score > int(main_records):
                #file.write(str(score))
                #best = 'Вы побили рекорд!'
            #else:
                #file.write(str(main_records))
            #result = f'Вы уничтожили: {str(score)} {best}'
            #lose_text = font.SysFont('Arial', 35).render(result, True, (255, 255, 255))
            #mw.blit(lose_text, (400, 325))

    display.update()
        #else:
            #finish = False
            #score = 0
            #miss = 0
            #for i in monsters:
                #i.kill()

            #time.delay(3000)
            #for i in range(20):
                #monster = Enemy('TIE.com.png', randint(80, 1120), randint(-100, -50), randint(1, 5), 80, 100)
                #monsters.add(monster)

time.delay(25)
