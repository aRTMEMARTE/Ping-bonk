from pygame import *


window = display.set_mode((700,500))
display.set_caption("Ping-bonk")
background = transform.scale(image.load('city.jpg'), (700, 500))

font.init()
font1 = font.Font(None, 100)
lose1 = font1.render('Player 1 LOSE!', True, (180, 0, 0))
lose2 = font1.render('Player 2 LOSE!', True, (180, 0, 0))

clock = time.Clock()
FPS = 60
speed_x = 3
speed_y = 3

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y >= 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y <= 295:
            self.rect.y += self.speed
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y >= 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y <= 295:
            self.rect.y += self.speed

player1 = Player('бита.png', 5, 250, 150, 200, 5)
player2 = Player('бита.png', 550, 250, 150, 200, 5)
ball = GameSprite('redball.png', 200, 200, 40, 40, 20)


finish = False
action = True
while action:
    for even in event.get():
        if even.type == QUIT:
            action = False
    
    if finish != True:
        window.blit(background, (0,0))
        player1.reset()
        player1.update_l()
        player2.reset()
        player2.update_r()
        ball.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y >= 495 or ball.rect.y <= 5:
            speed_y *= -1
        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            speed_x *= -1
        
        if ball.rect.x <= 0:
            finish = True
            window.blit(lose1, (200,200))
        if ball.rect.x >= 650:
            finish = True
            window.blit(lose2, (200,200))

    clock.tick(FPS)
    display.update()