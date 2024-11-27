import os
os.environ['SDL_VIDEODRIVER'] = 'x11'
import pygame
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()  # Initialize pygame first!
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
                
        screen.fill((0, 0, 0))
        
        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()