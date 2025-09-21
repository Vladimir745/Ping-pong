from pygame import *

back = (200, 255, 255)
width = 700
height = 500
window = display.set_mode((width, height))
display.set_caption('pygame window')
window.fill(back)

clock = time.Clock()
FPS = 60
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)