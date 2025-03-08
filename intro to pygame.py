import pygame
pygame.init()
screen = pygame.display.set_mode((500,400))
c=pygame.image.load("Untitled-1.jpg")
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.blit(c,(260,200))
    pygame.display.flip()