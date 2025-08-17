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
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

racket1 = Player('racket.png', 30, 200, 4, 50, 150) 
racket2 = Player('racket.png', 520, 200, 4, 50, 150)
ball = GameSprite('tenis_ball.png', 200, 200, 4, 50, 50)


run = True
clock = time.Clock()
fps = 60
""" program utama """
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    racket1.reset()
    racket2.reset()
    ball.reset()

    window.fill(background_color)
    display.update()
    clock.tick(fps)
