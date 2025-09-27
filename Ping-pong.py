from pygame import *

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
        if keys_pressed[K_w] and self.rect.x > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.x < width - 80:
            self.rect.y += self.speed
    def update_l(self):
        mouse_buttons = mouse.get_pressed()
        if mouse_buttons[0] and self.rect.x > 5:
            self.rect.y -= self.speed
        if mouse_buttons[2]:
            self.rect.y += self.speed

rocket1 = Player('rocket.png', 20, 250, 15, 100, 5)
rocket2 = Player('rocket.png', 680, 250, 15, 100, 5)
ball = Player('ball.png', 350, 250, 50, 50, 1.5)
font.init()
font = font.Font(None, 35)
lose1 = font.render('Игрок 1 проиграл!', True, (180, 0, 0))
lose2 = font.render('Игрок 2 проиграл!', True, (180, 0, 0))
back = (200, 255, 255)
width = 700
height = 500
window = display.set_mode((width, height))
display.set_caption('pygame window')

clock = time.Clock()
FPS = 60
game = True
finish = False

speed_x = 5
speed_y = 5

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        rocket1.update_r()
        rocket2.update_l()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(rocket1, ball) or  sprite.collide_rect(rocket2, ball):
            speed_x *= -1
            speed_y *= 1
        if ball.rect.y == height or ball.rect.y == 0:
            speed_y *= -1
        if ball.rect.x >= width:
            finish = True
            window.blit(lose2, (200, 200))
            game_over = True
        if ball.rect.x <= 0:
            finish = True
            window.blit(lose1, (200, 200))
            game_over = True
        rocket1.reset()
        rocket2.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)
