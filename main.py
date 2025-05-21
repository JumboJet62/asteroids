import sys
import pygame
from constants import *
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    

    player = Player((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
    
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        
        updatable.update(dt)
        for drawable_object in drawable:
            drawable_object.draw(screen)
        
        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game over!")
                sys.exit()
            
        
        for asteroid in asteroids:
            for shot in shots:
                if shot.check_collision(asteroid):
                    shot.kill()
                    asteroid.split()


        pygame.display.flip()
        
        # framerate limiter locked at 60 fps
        dt = game_clock.tick(60) / 1000
        
if __name__ == "__main__":
    main()