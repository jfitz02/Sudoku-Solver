import pygame
import time
from sudokusolver import solver, check_row, check_col, check_box

display_width = 200
display_height = 300

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255, 0, 0)
GREEN = (0,255,0)
BLUE = (0,0,255)
PINK = (245, 0,255)
PURPLE = (150, 0, 150)

refresh = True
grid = [[0 for i in range(9)] for i in range(9)]


pygame.init()

gameDisplay = pygame.display.set_mode((display_width, display_height))

def button(current, number, x, y, selection=True, position = None, array = None):
    global refresh, grid
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if selection:
        width = 20
        height = 40
        if current == number:
            message_display(str(number), x+(width/2), y+(height/2), 24, GREEN)
        else:
            if (x<mouse[0]<x+width) and (y<mouse[1]<y+height):
                message_display(str(number), x+(width/2), y+(height/2), 24, PINK)
                if click[0] == 1:
                    return number
            else:
                message_display(str(number), x+(width/2), y+(height/2), 24, BLUE)
        return current
    else:
        width = 20
        height = 20
        if (x<mouse[0]<x+width) and (y<mouse[1]<y+height):
            if click[0] == 1:
                if (check_col(grid, position[1], current) and check_row(grid, position[0], current) and check_box(grid, position[0],position[1], current)) or current == 0:
                    print("yes")
                    refresh = True
                    array[position[0]][position[1]] = current
                    
        return array

def solve_button(grid):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    x = 5
    y = 250
    w = 90
    h = 40
    
    pygame.draw.rect(gameDisplay, RED, [x, y, w, h])
    message_display("solve", 47, 270, 20, PURPLE, solve_button = True)
    
    if (x<mouse[0]<x+w) and (y<mouse[1]<y+h):
        if click[0] == 1:
            return solver(grid), True
    return grid, False
def message_display(text, x, y, fontsize, colour, solve_button = False):
    largeText = pygame.font.Font('freesansbold.ttf',fontsize)
    TextSurf, TextRect = text_objects(text, largeText, colour)
    TextRect.center = ((x),(y))
    gameDisplay.blit(TextSurf, TextRect)
    if solve_button == False:
        pygame.display.update(x-10, y-10, 20, 20)
    else:
        pygame.display.update(x-45, y-20, 90, 40)

def text_objects(text, font, colour):
    textSurface = font.render(text, True, colour)
    return textSurface, textSurface.get_rect()

def draw_grid(grid):
    gameDisplay.fill(WHITE)
    thickness = 2
    length = 194
    for i in range(4):
        x = (64*i)+3
        y = 3
        pygame.draw.rect(gameDisplay, BLACK, [x,y, thickness, length])
        pygame.draw.rect(gameDisplay, BLACK, [y,x,length, thickness])
    thickness = 1
    
    j = 0
    for i in range(10):
        if i not in (0,3,6,9):
            x = (21*i)+3+j
            pygame.draw.rect(gameDisplay, BLACK, [x,y, thickness, length])
            pygame.draw.rect(gameDisplay, BLACK, [y,x,length, thickness])
        else:
            j+=1

    positions = [15,36,57,79,100,121,143,164,185]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != 0:
                message_display(str(grid[i][j]), positions[i], positions[j], 12, RED)
            
            
def main():
    global refresh, grid
    number = 1
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                
        for i in range(10):
            value = button(number, i, ((20*i)+10)-10, 190)
            if value != number:
                number = value

        pos_0 = 5
        for i in range(9):
            pos_1 = 5
            for j in range(9):
                grid = button(number, "", pos_0,pos_1, selection = False, array = grid, position = [i,j])
                pos_1+=21
                if (j+1)%3==0:
                    pos_1+=1
            if (i+1)%3==0:
                pos_0+=1
            pos_0+=21
            
        if refresh:
            draw_grid(grid)
            pygame.display.update()
            refresh = False

        grid, refresh = solve_button(grid) 
            
main()
