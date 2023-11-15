"""
Simulation of a tree data structure in pygame
Operations:
- search
- insert a node
- delete
Author: Wesin Ribeiro
"""

import pygame
import random
import rb_tree
# setup
# pygame setup
pygame.init()
# create screen
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Simulação de Árvores Binárias RB")
clock = pygame.time.Clock()
running = True
dt = 0
tree = rb_tree.RBTree()

player_pos = pygame.Vector2(screen.get_width() / 2, 100)
numbers = [random.randint(0, 100) for i in range(10)]
i = 0

# add instructions in screen
def draw_instructions():
    font = pygame.font.SysFont("Arial", 12, )
    instructions = [
        "Pressione D para inserir um número",
        "Pressione A para remover um número a raiz",
        "Pressione ESPAÇO para gerar 10 números",
        "Pressione ESC para sair"
    ]
    for i, instruction in enumerate(instructions):
        instruction_img = font.render(instruction, True, "blue")
        instruction_rect = instruction_img.get_rect()
        instruction_rect.x = (30)
        instruction_rect.y = (50 + 15 * i)
    
        screen.blit(instruction_img, instruction_rect)
## generate 10 numbers
## draw numbers
def draw_numbers(numbers):
    font = pygame.font.SysFont("Arial", 20)
    numbers_str = ', '.join([str(n) for n in numbers])
    numbers_img = font.render(numbers_str, True, "black")
    numbers_rect = numbers_img.get_rect()
    numbers_rect.center = (screen.get_width() / 2, 40)
    screen.blit(numbers_img, numbers_rect)

def draw_tree(node, level, xpos, is_left, length=120):
    if node.key is None:
        return
    
    # draw node
    color = "grey"
    if node.color == "RED":
        color = "red"

    # draw message
    font = pygame.font.SysFont("Arial", 20)
    node_str = str(node.key)
    node_img = font.render(node_str, True, "black")
    node_rect = node_img.get_rect()
    if node is tree.root:
        node_rect.x = xpos
    else:
        if is_left:
            xpos = xpos - length * (level + 1)
            node_rect.x = xpos
        else:
            xpos = xpos + length * (level + 1)
            node_rect.x = xpos
    
    node_rect.y = (100 + 40 * level)

    # draw line
    if node is not tree.root:
        #pygame.draw.line(screen, "green", (pos + 10, (100 + 100 * level) + 10), (pos + 10, (100 + 100 * (level - 1)) + 10))
        start = (xpos + 10, (100 + 40 * level) + 10)
        if is_left:
            end = (xpos + 10 + length * (level + 1), (100 + 40 * (level - 1)) + 10)
            pygame.draw.line(screen, "blue", start, end)
        else:
            end = (xpos + 10 - length * (level + 1), (100 + 40 * (level - 1)) + 10)
            pygame.draw.line(screen, "black", start, end)

    # draw circle
    pygame.draw.circle(screen, color, (xpos+10, (100 + 40 * level) + 10), 20)

    screen.blit(node_img, node_rect)


    draw_tree(node.left, level + 1, xpos, True, length//2)
    draw_tree(node.right, level + 1, xpos, False, length//2)


# run loop

while running:
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")
    draw_instructions()
    draw_numbers(numbers)
    if tree.root.key is not None:
        draw_tree(tree.root, 0, screen.get_width() / 2, True)

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                numbers = [random.randint(0, 100) for i in range(10)]
                i = 0
                tree = rb_tree.RBTree()
                draw_tree(tree.root, 0, screen.get_width() / 2, True)
            elif event.key == pygame.K_a:
                if i > 0:
                    i = i - 1
                    tree.remove(tree.root)
                    draw_tree(tree.root, 0, screen.get_width() / 2, True)
                
            elif event.key == pygame.K_d: 
                if i < 10:
                    tree.insert(numbers[i])
                    draw_tree(tree.root, 0, screen.get_width() / 2, True)
                    i = i + 1

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()