from pygame import *

win_width = 600
win_height = 500

""" set tampilan """
window = display.set_mode((win_width, win_height))
display.set_caption('ping pong mudah')

background_color = (255, 255, 255)
window.fill(background_color)

class GameSprite(sprite.Sprite):
#class constructor
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        #Call for the class (Sprite) constructor:
        sprite.Sprite.__init__(self)


        #every sprite must store the image property
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed


        #every sprite must have the rect property – the rectangle it is fitted in
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
#method drawing the character on the window
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


#main player class
class Player(GameSprite):
   #method to control the sprite with arrow keys
    def update_racket_2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

    def update_racket_1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed


racket1 = Player('racket.png', 30, 200, 30, 100, 5)
racket2 = Player('racket.png', 520, 200, 30, 100, 5)
ball = GameSprite('tennis_ball.png', 270, 230, 50, 50, 50)

font.init()
font = font.Font(None, 35)
lose_1 = font.render('PLAYER 1 LOSE', True, (180, 0, 0))
lose_2 = font.render('PLAYER 2 LOSE', True, (180, 0, 0))

speed_x = 3
speed_y = 3

run = True
finish = False
clock = time.Clock()
fps = 60
""" program utama """
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if finish != True:
        window.fill(background_color)

        racket1.update_racket_1()
        racket2.update_racket_2()


        #ball move
        ball.rect.x +=  speed_x
        ball.rect.y +=  speed_y

        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y = speed_y * -1

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= 1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose_1, (200, 200))

        if ball.rect.x > win_width:
            finish = True
            window.blit(lose_2, (200, 200))


    racket1.reset()
    racket2.reset()
    ball.reset()

    
    display.update()
    clock.tick(fps)
