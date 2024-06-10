import pygame 
import sys
import math


# init pygame 

pygame.init()

# draw a 600 x 600 window
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("BOUNCY BOUNCY!")

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)


class DrawCircle:
    def __init__(self):
        self.center = (300,300)
        self.radius = 255
        self.width = 3 
    
    def draw(self):
        pygame.draw.circle(screen,WHITE, self.center,self.radius,self.width)


class BouncingBall:
    def __init__(self):
        self.x = 300  
        self.y = 300
        self.velocity = [2,3]  
        self.radius =  15

    def move(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]

        if self.distance_to_center() + self.radius > 225:
            # calculate the normal vector at the point of collision
            normal = [self.x - 300, self.y -300]
            normal_length = math.sqrt(normal[0] ** 2 + normal[1] ** 2)
            normal = [normal[0] / normal_length, normal[1]/int(normal_length)]

            # reflect the ball's velocty aroun the normal vector

            dot_product = self.velocity[0] * normal[0] + self.velocity[1] * normal[1]

            self.velocity[0] -= 2 * dot_product * normal[0]
            self.velocity[1] -= 2 * dot_product * normal[1]

    def distance_to_center(self):
        return math.sqrt((self.x - 300) ** 2 + (self.y - 300) ** 2)

    def draw(self):
        pygame.draw.circle(screen, RED, (int(self.x), int(self.y)), self.radius)

# Create instances
circle = DrawCircle()
ball = BouncingBall()

# Game loop
while 1==1:
    # Move the ball
    ball.move()

    # Clear the screen
    screen.fill(BLACK)

    # Draw the circle and the ball
    circle.draw()
    ball.draw()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

