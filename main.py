import pygame
import algorithms as al
from visuals import draw
from rectangle_class import make_rects

pygame.init()
total_rects = 20
WIDTH = 600
HEIGHT = 350

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Visual Sorting Algorithms')

def main(win):
    run = True
    execute = False
    ascending = True
    algo = 'Insert'
    rect_row = make_rects()

    draw(win, rect_row, algo, ascending)

    while run:
        keys = pygame.key.get_pressed()
        mx, my = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                pygame.quit() 
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Sorting options for tab
                if mx in range(315, 375) and my in range(41):
                    algo = 'Merge'

                elif mx in range(5, 55) and my in range(41):
                    algo = 'Insert'

                elif mx in range(70, 135) and my in range(41):
                    algo = 'Bubble'

                elif mx in range(150, 230) and my in range(41):
                    algo = 'Selection'

                elif mx in range(245, 300) and my in range(41):
                    algo = 'Quick'

                # Sorting order options for tab
                elif mx in range(405, 490) and my in range(41):
                    ascending = True

                elif mx in range(505, 600) and my in range(41):
                    ascending = False

        # Key for reset
        if keys[pygame.K_r]:
            new_list = make_rects()
            rect_row = new_list

        if keys[pygame.K_SPACE]:   
            execute = True

        if execute == False:
            draw(win, rect_row, algo, ascending)
        
        # To show to sorting visual
        if execute == True:
            # Sorting options for execution
            if algo == 'Quick':   
                al.quickSort(win, rect_row, 0, total_rects - 1, ascending)

            elif algo == 'Merge':
                al.mergeSort(win, rect_row, ascending)

            elif algo == 'Insert':
                al.insertionSort(win, rect_row, ascending)

            elif algo == 'Bubble':
                al.bubbleSort(win, rect_row, ascending)

            elif algo == 'Selection':
                al.selectionSort(win, rect_row, ascending)

            execute = False

    pygame.quit()

main(WIN)