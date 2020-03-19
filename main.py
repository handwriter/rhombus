import pygame


pygame.init()
n = int(input())
size = width, height = 155, 155
screen = pygame.display.set_mode(size)
screen.fill((255, 255, 0))
# ожидание закрытия окна:
counters = 0
for i in range(0, width, width // n):
    counters += 1
    counter = 0
    for j in range(0, height, height // n):
        counter += 1
        if i + width // n > width or j + height // n > height:
            break
        pygame.draw.polygon(screen, (255, 165, 0), ((i, j + height // n // 2), (i + width // n // 2, j),
                                                    (i + width // n, j + height // n // 2),
                                                    (i + width // n // 2, j + height // n)))
        if counter == n:
            break
    if counters == n:
        break
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()