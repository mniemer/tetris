import os, sys
import pygame
from pygame.locals import *

from game_utility import *
from board import Board
from block import Block, Mino

SCREEN_SIZE = 500, 800

# TODO: fix bugs with line clearing(should be good), hard drop
# TODO: add game over
# TODO: add score, clock, up next queue, holds, pictures
# TODO: fix rotation stuff
# TODO: problem with keyboard input

def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("TETRIS")

    clock = pygame.time.Clock()
    time = 0
    timeLimit = 2000 #2000 milliseconds = 2 seconds
    dropOne = False

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))
    board = Board()
    boardPanel = pygame.sprite.Group(board)
    newMino = True

    while 1:
        clock.tick()
        time += clock.get_time()

        if newMino:
            mino = Mino(board)
            newMino = False

        if time >= timeLimit:
            dropOne = True
            time = 0

        moveDir = None
        rotateDir = None
        hardDrop = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[K_ESCAPE]:
                    return
                if keys[K_DOWN]:
                    hardDrop = True
                elif keys[K_UP]:
                    moveDir = DOWN
                elif keys[K_RIGHT]:
                    moveDir = RIGHT
                elif keys[K_LEFT]:
                    moveDir = LEFT
                if keys[K_x]:
                    rotateDir = COUNTERCLOCK #TODO: fix the rotation mechanics
                elif keys[K_z]:
                    rotateDir = CLOCK

        newMino = mino.updateMino(hardDrop, dropOne, moveDir, rotateDir)
        if dropOne:
            dropOne = False

        mino.blockGroup.update()
        board.clearLines()

        screen.blit(background, (0, 0))
        boardPanel.draw(screen)
        board.blockGroup.draw(screen)
        mino.blockGroup.draw(screen)
        pygame.display.flip()

if __name__ == '__main__': main()
