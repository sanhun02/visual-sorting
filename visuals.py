import pygame

pygame.init()
WIDTH = 600
WHITE = (255, 255, 255)

font = pygame.font.Font('freesansbold.ttf', 13)
sortTxt = font.render('Insert    |    Bubble    |    Selection    |    Quick    |    Merge', 
                            True, WHITE, None)

orderTxt = font.render('Ascending    |    Descending', 
                            True, WHITE, None)

alertTxt = font.render('(hold/press space bar to sort)     (hold/press R to reset bars)     (press esc to exit)', 
                            True, (0, 0, 0), None)

def clock(tick_num):
    c = pygame.time.Clock()
    c.tick(tick_num)

def draw(win, rect_row, algo, ascending):
    win.fill(WHITE)
    pygame.draw.rect(win, (0, 0, 0), (0, 0, WIDTH, 40))
    win.blit(sortTxt, (10, 15))
    win.blit(orderTxt, (415, 15))
    win.blit(alertTxt, (50, 45))
     
    title = pygame.font.Font('freesansbold.ttf', 16).render(f"{algo} - {'Ascending' if ascending else 'Descending'}",
                                True, (0, 0, 0), None)
    win.blit(title, (240, 75))

    draw_rect(win, rect_row, 60, False)
    pygame.display.update()

def draw_rect(win, rect_row, tick, clear_bg=False):
    clock(tick)

    if clear_bg:
        clear_rect = (0, 100, WIDTH, 250)
        pygame.draw.rect(win, WHITE, clear_rect)

    for rect in rect_row:
        rect.draw(win)

    if clear_bg:
        pygame.display.update()