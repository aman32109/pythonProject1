from pygame import init, display,QUIT, event
init()
screen = display.set_mode((400, 500))
done = False

while not done:
    for event in event.get():
        if event.type == exit():
            done = True
    display.flip()
