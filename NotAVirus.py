import pygame, random, pyautogui

screen = pygame.display.set_mode((1300,700), pygame.FULLSCREEN)
pyautogui.FAILSAFE = False
draw_on = False
radius = 10

def roundline(srf, color, start, end, radius=1):
    dx = end[0]-start[0]
    dy = end[1]-start[1]
    distance = max(abs(dx), abs(dy))
    for i in range(distance):
        x = int( start[0]+float(i)/distance*dx)
        y = int( start[1]+float(i)/distance*dy)
        pygame.draw.circle(srf, color, (x, y), radius)

def draw(x):
    color = (255,255,255)
    xd = 100
    yd = 100
    last_pos = (xd, yd)
    pyautogui.mouseDown()
    
    pyautogui.moveTo(xd, yd)
    pygame.draw.circle(screen, (255,255,255), (xd, yd), 1)
    
    pyautogui.moveRel(x, 0)
    pygame.draw.circle(screen, color, pyautogui.position(), radius)
    roundline(screen, color, pyautogui.position(), last_pos,  radius)
    last_pos = pyautogui.position()
    pygame.display.flip()
    
    pyautogui.moveRel(0, -x)
    pygame.draw.circle(screen, color, pyautogui.position(), radius)
    roundline(screen, color, pyautogui.position(), last_pos,  radius)
    last_pos = pyautogui.position()
    pygame.display.flip()
    
    pyautogui.moveRel(-x, 0)
    pygame.draw.circle(screen, color, pyautogui.position(), radius)
    roundline(screen, color, pyautogui.position(), last_pos,  radius)
    last_pos = pyautogui.position()
    pygame.display.flip()
    
    pyautogui.moveRel(0,x)
    pygame.draw.circle(screen, color, pyautogui.position(), radius)
    roundline(screen, color, pyautogui.position(), last_pos,  radius)
    last_pos = pyautogui.position()
    pygame.display.flip()
    
    pyautogui.moveRel((x * 4), 0)
    pygame.draw.circle(screen, color, pyautogui.position(), radius)
    roundline(screen, color, pyautogui.position(), last_pos,  radius)
    last_pos = pyautogui.position()
    pygame.display.flip()
    
    pyautogui.moveRel(0, x)
    pygame.draw.circle(screen, color, pyautogui.position(), radius)
    roundline(screen, color, pyautogui.position(), last_pos,  radius)
    last_pos = pyautogui.position()
    pygame.display.flip()
    
    pyautogui.moveRel(-(x * 4), 0)
    pygame.draw.circle(screen, color, pyautogui.position(), radius)
    roundline(screen, color, pyautogui.position(), last_pos,  radius)
    last_pos = pyautogui.position()
    pygame.display.flip()
    
    pyautogui.moveRel(0, x)
    pygame.draw.circle(screen, color, pyautogui.position(), radius)
    roundline(screen, color, pyautogui.position(), last_pos,  radius)
    last_pos = pyautogui.position()
    pygame.display.flip()
    
    pyautogui.moveRel(x, 0)
    pygame.draw.circle(screen, color, pyautogui.position(), radius)
    roundline(screen, color, pyautogui.position(), last_pos,  radius)
    last_pos = pyautogui.position()
    pygame.display.flip()
    
    pyautogui.moveRel(0, -(x * 3))
    pygame.draw.circle(screen, color, pyautogui.position(), radius)
    roundline(screen, color, pyautogui.position(), last_pos,  radius)
    last_pos = pyautogui.position()
    pygame.display.flip()
    
    pyautogui.moveRel(-x, 0)
    pygame.draw.circle(screen, color, pyautogui.position(), radius)
    roundline(screen, color, pyautogui.position(), last_pos,  radius)
    last_pos = pyautogui.position()
    pygame.display.flip()
    
    pyautogui.moveRel(0, x)
    pygame.draw.circle(screen, color, pyautogui.position(), radius)
    roundline(screen, color, pyautogui.position(), last_pos,  radius)
    last_pos = pyautogui.position()
    pygame.display.flip()
    

    pyautogui.moveRel(0 , x*7)
    pygame.draw.circle(screen, color, pyautogui.position(), radius)
    roundline(screen, color, pyautogui.position(), last_pos,  radius)
    last_pos = pyautogui.position()
    pygame.display.flip()
    
    pyautogui.moveTo(xd, yd + (x*7))
    pygame.draw.circle(screen, color, pyautogui.position(), radius)
    roundline(screen, color, pyautogui.position(), last_pos,  radius)
    last_pos = pyautogui.position()
    pygame.display.flip()
    

    pyautogui.moveRel(x, 0)
    pygame.draw.circle(screen, color, pyautogui.position(), radius)
    roundline(screen, color, pyautogui.position(), last_pos,  radius)
    last_pos = pyautogui.position()
    pygame.display.flip()
    
    pyautogui.moveRel(0, -x * 3)
    pygame.draw.circle(screen, color, pyautogui.position(), radius)
    roundline(screen, color, pyautogui.position(), last_pos,  radius)
    last_pos = pyautogui.position()
    pygame.display.flip()
    
    pyautogui.moveRel(-x, 0)
    pygame.draw.circle(screen, color, pyautogui.position(), radius)
    roundline(screen, color, pyautogui.position(), last_pos,  radius)
    last_pos = pyautogui.position()
    pygame.display.flip()
    
    pyautogui.moveRel(0, x)
    pygame.draw.circle(screen, color, pyautogui.position(), radius)
    roundline(screen, color, pyautogui.position(), last_pos,  radius)
    last_pos = pyautogui.position()
    pygame.display.flip()
    
    pyautogui.moveRel(x * 4, 0)
    pygame.draw.circle(screen, color, pyautogui.position(), radius)
    roundline(screen, color, pyautogui.position(), last_pos,  radius)
    last_pos = pyautogui.position()
    pygame.display.flip()
    
    pyautogui.moveRel(0, x)
    pygame.draw.circle(screen, color, pyautogui.position(), radius)
    roundline(screen, color, pyautogui.position(), last_pos,  radius)
    last_pos = pyautogui.position()
    pygame.display.flip()
    
    pyautogui.moveRel(-x * 4, 0)
    pygame.draw.circle(screen, color, pyautogui.position(), radius)
    roundline(screen, color, pyautogui.position(), last_pos,  radius)
    last_pos = pyautogui.position()
    pygame.display.flip()
    
    
    pyautogui.moveRel(0, -x * 6)
    pygame.draw.circle(screen, color, pyautogui.position(), radius)
    roundline(screen, color, pyautogui.position(), last_pos,  radius)
    last_pos = pyautogui.position()
    pygame.display.flip()

    #-------------
    pyautogui.moveTo(xd, yd)
    pygame.draw.circle(screen, (255,255,255), (xd, yd), 1)
    
    pyautogui.moveRel(x, 0)
    pygame.draw.circle(screen, color, pyautogui.position(), radius)
    roundline(screen, color, pyautogui.position(), last_pos,  radius)
    last_pos = pyautogui.position()
    pygame.display.flip()
    
    pyautogui.moveRel(0, -x)
    pygame.draw.circle(screen, color, pyautogui.position(), radius)
    roundline(screen, color, pyautogui.position(), last_pos,  radius)
    last_pos = pyautogui.position()
    pygame.display.flip()
    
    pyautogui.moveRel(-x, 0)
    pygame.draw.circle(screen, color, pyautogui.position(), radius)
    roundline(screen, color, pyautogui.position(), last_pos,  radius)
    last_pos = pyautogui.position()
    pygame.display.flip()
    
    pyautogui.moveRel(0,x)
    pygame.draw.circle(screen, color, pyautogui.position(), radius)
    roundline(screen, color, pyautogui.position(), last_pos,  radius)
    last_pos = pyautogui.position()
    pygame.display.flip()
    
    pyautogui.moveRel((x * 4), 0)
    pygame.draw.circle(screen, color, pyautogui.position(), radius)
    roundline(screen, color, pyautogui.position(), last_pos,  radius)
    last_pos = pyautogui.position()
    pygame.display.flip()
    
    pyautogui.moveRel(0, x)
    pygame.draw.circle(screen, color, pyautogui.position(), radius)
    roundline(screen, color, pyautogui.position(), last_pos,  radius)
    last_pos = pyautogui.position()
    pygame.display.flip()
    
    pyautogui.moveRel(-(x * 4), 0)
    pygame.draw.circle(screen, color, pyautogui.position(), radius)
    roundline(screen, color, pyautogui.position(), last_pos,  radius)
    last_pos = pyautogui.position()
    pygame.display.flip()
    
    pyautogui.moveRel(0, x)
    pygame.draw.circle(screen, color, pyautogui.position(), radius)
    roundline(screen, color, pyautogui.position(), last_pos,  radius)
    last_pos = pyautogui.position()
    pygame.display.flip()
    
    pyautogui.moveRel(x, 0)
    pygame.draw.circle(screen, color, pyautogui.position(), radius)
    roundline(screen, color, pyautogui.position(), last_pos,  radius)
    last_pos = pyautogui.position()
    pygame.display.flip()
    
    pyautogui.moveRel(0, -(x * 3))
    pygame.draw.circle(screen, color, pyautogui.position(), radius)
    roundline(screen, color, pyautogui.position(), last_pos,  radius)
    last_pos = pyautogui.position()
    pygame.display.flip()
    
    pyautogui.moveRel(-x, 0)
    pygame.draw.circle(screen, color, pyautogui.position(), radius)
    roundline(screen, color, pyautogui.position(), last_pos,  radius)
    last_pos = pyautogui.position()
    pygame.display.flip()
    
    pyautogui.moveRel(0, x)
    pygame.draw.circle(screen, color, pyautogui.position(), radius)
    roundline(screen, color, pyautogui.position(), last_pos,  radius)
    last_pos = pyautogui.position()
    pygame.display.flip()
    

    pyautogui.moveRel(0 , x*7)
    pygame.draw.circle(screen, color, pyautogui.position(), radius)
    roundline(screen, color, pyautogui.position(), last_pos,  radius)
    last_pos = pyautogui.position()
    pygame.display.flip()
    
    pyautogui.moveTo(xd, yd + (x*7))
    pygame.draw.circle(screen, color, pyautogui.position(), radius)
    roundline(screen, color, pyautogui.position(), last_pos,  radius)
    last_pos = pyautogui.position()
    pygame.display.flip()
    

    pyautogui.moveRel(x, 0)
    pygame.draw.circle(screen, color, pyautogui.position(), radius)
    roundline(screen, color, pyautogui.position(), last_pos,  radius)
    last_pos = pyautogui.position()
    pygame.display.flip()
    
    pyautogui.moveRel(0, -x * 3)
    pygame.draw.circle(screen, color, pyautogui.position(), radius)
    roundline(screen, color, pyautogui.position(), last_pos,  radius)
    last_pos = pyautogui.position()
    pygame.display.flip()
    
    pyautogui.moveRel(-x, 0)
    pygame.draw.circle(screen, color, pyautogui.position(), radius)
    roundline(screen, color, pyautogui.position(), last_pos,  radius)
    last_pos = pyautogui.position()
    pygame.display.flip()
    
    pyautogui.moveRel(0, x)
    pygame.draw.circle(screen, color, pyautogui.position(), radius)
    roundline(screen, color, pyautogui.position(), last_pos,  radius)
    last_pos = pyautogui.position()
    pygame.display.flip()
    
    pyautogui.moveRel(x * 4, 0)
    pygame.draw.circle(screen, color, pyautogui.position(), radius)
    roundline(screen, color, pyautogui.position(), last_pos,  radius)
    last_pos = pyautogui.position()
    pygame.display.flip()
    
    pyautogui.moveRel(0, x)
    pygame.draw.circle(screen, color, pyautogui.position(), radius)
    roundline(screen, color, pyautogui.position(), last_pos,  radius)
    last_pos = pyautogui.position()
    pygame.display.flip()
    
    pyautogui.moveRel(-x * 4, 0)
    pygame.draw.circle(screen, color, pyautogui.position(), radius)
    roundline(screen, color, pyautogui.position(), last_pos,  radius)
    last_pos = pyautogui.position()
    pygame.display.flip()
    
    
    pyautogui.moveRel(0, -x * 6)
    pygame.draw.circle(screen, color, pyautogui.position(), radius)
    roundline(screen, color, pyautogui.position(), last_pos,  radius)
    last_pos = pyautogui.position()
    pygame.display.flip()

    pyautogui.mouseUp()



try:
    while True:
        draw(70)

except StopIteration:
    pass

pygame.quit()


