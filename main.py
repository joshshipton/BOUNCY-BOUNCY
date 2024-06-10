import pygame
import sys
import math
import random
from enum import Enum

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("BOUNCY BOUNCY!")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Color(Enum):
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    YELLOW = (255, 255, 0)
    CYAN = (0, 255, 255)
    MAGENTA = (255, 0, 255)

    @staticmethod
    def random_color():
        return random.choice(list(Color))

class BouncingBall:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.velocity = [random.uniform(-2, 2), random.uniform(-2, 2)]  # Random initial velocity
        self.radius = radius
        self.color = color
        self.gravity = 0.1  # Gravity acceleration

    def move(self):
        # Apply gravity
        self.velocity[1] += self.gravity
        self.x += self.velocity[0]
        self.y += self.velocity[1]

        # Check for collision with the boundary of the larger circle
        if self.distance_to_center() + self.radius > 225:
            normal = [self.x - 300, self.y - 300]
            normal_length = math.sqrt(normal[0] ** 2 + normal[1] ** 2)
            normal = [normal[0] / normal_length, normal[1] / normal_length]
            dot_product = self.velocity[0] * normal[0] + self.velocity[1] * normal[1]
            self.velocity[0] -= 2 * dot_product * normal[0]
            self.velocity[1] -= 2 * dot_product * normal[1]

    def distance_to_center(self):
        return math.sqrt((self.x - 300) ** 2 + (self.y - 300) ** 2)

    def draw(self):
        pygame.draw.circle(screen, self.color.value, (int(self.x), int(self.y)), self.radius)

# Create the larger circle
class DrawCircle:
    def __init__(self):
        self.center = (300, 300)
        self.radius = 225
        self.width = 3

    def draw(self):
        pygame.draw.circle(screen, WHITE, self.center, self.radius, self.width)

# Check collision between two balls
def check_collision(ball1, ball2):
    distance = math.sqrt((ball1.x - ball2.x) ** 2 + (ball1.y - ball2.y) ** 2)
    return distance < ball1.radius + ball2.radius

# Resolve collision between two balls
def resolve_collision(ball1, ball2):
    normal = [ball2.x - ball1.x, ball2.y - ball1.y]
    distance = math.sqrt(normal[0] ** 2 + normal[1] ** 2)
    if distance == 0:
        return

    normal = [normal[0] / distance, normal[1] / distance]
    relative_velocity = [ball1.velocity[0] - ball2.velocity[0], ball1.velocity[1] - ball2.velocity[1]]
    velocity_along_normal = relative_velocity[0] * normal[0] + relative_velocity[1] * normal[1]

    if velocity_along_normal > 0:
        return

    restitution = 1 
    impulse = -(1 + restitution) * velocity_along_normal
    impulse /= (1 / ball1.radius + 1 / ball2.radius)

    impulse_vector = [impulse * normal[0], impulse * normal[1]]
    ball1.velocity[0] += impulse_vector[0] / ball1.radius
    ball1.velocity[1] += impulse_vector[1] / ball1.radius
    ball2.velocity[0] -= impulse_vector[0] / ball2.radius
    ball2.velocity[1] -= impulse_vector[1] / ball2.radius

    # Move balls apart to prevent overlap
    overlap = 0.5 * (ball1.radius + ball2.radius - distance + 1)
    ball1.x -= overlap * normal[0]
    ball1.y -= overlap * normal[1]
    ball2.x += overlap * normal[0]
    ball2.y += overlap * normal[1]

    # Change colors on collision
    ball1.color = Color.random_color()
    ball2.color = Color.random_color()
    ball1.radius += 1
    ball2.radius += 1 

# Create instances
circle = DrawCircle()
balls = [BouncingBall(random.randint(200, 400), random.randint(100, 400), 20, Color.random_color()) for _ in range(2)]

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move balls
    for ball in balls:
        ball.move()

    # Handle collisions between balls
    for i in range(len(balls)):
        for j in range(i + 1, len(balls)):
            if check_collision(balls[i], balls[j]):
                resolve_collision(balls[i], balls[j])

    # Clear the screen
    screen.fill(BLACK)

    # Draw the circle and the balls
    circle.draw()
    for ball in balls:
        ball.draw()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()

