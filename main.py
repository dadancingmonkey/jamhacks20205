import pygame
import sys
import gamesprites
import random


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Game Title")
        self.clock = pygame.time.Clock()
        self.running = True

        self.entities()
        self.gameloop()
        self.refresh()

    def entities(self):
        # Sprite groups
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.trees = pygame.sprite.Group()

        # Example: Add a player
        self.player = gamesprites.Player((400, 300))
        self.all_sprites.add(self.player, layer=2)

        # Example: Add a tree
        tree = gamesprites.Tree((200, 400))
        self.trees.add(tree)
        self.all_sprites.add(tree, layer=1)

    def refresh(self):
        self.screen.fill((135, 206, 235))  # Light sky blue background

        # Draw all sprites (will respect layers)
        self.all_sprites.draw(self.screen)

        pygame.display.flip()

    def gameloop(self):
        while self.running:
            dt = self.clock.tick(60) / 1000  # Delta time in seconds

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Update all sprites (pass dt if needed)
            self.all_sprites.update(dt)

            # Refresh display
            self.refresh()

        pygame.quit()
        sys.exit()

game = Game()