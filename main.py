from random import randint
from pygame import *
from time import time as timer
class Gamesprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(Gamesprite):
    def updater(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < window_h - 80:
            self.rect.y += self.speed
    def updatel(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < window_h - 80:
            self.rect.y += self.speed

window_w = 700
window_h = 500
window = display.set_mode((window_w, window_h))
display.set_caption('ААААААА, не пингуй')

background = transform.scale(image.load('kakoytophon.png'), (window_w, window_h))

player = Player('vroderacketka.png', 25, window_h - 100, 15, 50, 10)
player0 = Player('vroderacketka.png', window_w - 40, 100, 15, 50, 10)

clock = time.Clock()
gm = True
finish = False
FPS = 60
while gm:
    for e in event.get():
        if e.type == QUIT:
            gm = False
    if not finish:
        window.blit(background,(0, 0))
        player.updatel()
        player0.updater()
        player.reset()
        player0.reset()
    display.update()
    clock.tick(FPS)