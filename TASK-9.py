import pygame
import sys

pygame.init()
size_block = 100
mar = 15
width = heigth = size_block*3 + mar*4

size_window = (width,heigth)
screen = pygame.display.set_mode(size_window)
pygame.display.set_caption("")

black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
white = (255,255,255)
mas = [[0]*3 for i in range(3)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            col = x_mouse // (size_block+mar)
            row = y_mouse // (size_block+mar)
            mas[row][col] = "x"
               
    
    for row in range(3):
        for col in range(3):
            if mas [row] [col] == "x":
                color = red
            else:
                color = white
                
            x = col*size_block + (col+1)*mar
            y = row*size_block + (row+1)*mar
            pygame.draw.rect(screen, color, (x, y, size_block,size_block))
            
            pygame.display.update() 