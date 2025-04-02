from pygame import *

window = display.set_mode((700,500))
fon = (0, 255, 149)
window.fill(fon)
clock = time.Clock()
fps = 60



game = True
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
    display.update()
    clock.tick(fps)