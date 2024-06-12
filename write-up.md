Recently [this video](https://www.youtube.com/watch?v=Mu6hloC7ty8&ab_channel=GreenCode) came up on my YouTube, I liked the idea of making satisfied simulations with code so I thought I would try it for myself. This ended up being the first time I ever  used high school math in real life, and I loved it. 

I'm going to walk through the steps that it took to get the foundation of these simulations going, it's not perfect but the meat and potatoes are there. By the end you'll be able to simulate some basic physics and have something that looks like this. 

Video here

For this simulation I'm going to be using pygame, pygame is a nifty little library that makes it really easy to run simulations like these ones and get visual stuff up on the screen super quick whilst using all that python syntax that we all know and love. 

Here's some boiler plate code, to initialize pygame, draw a screen and define some colors. This isn't really too relevant or interesting but I've included it for transparency. 

```python
import pygame 
import math


# init pygame 

pygame.init()

# draw a 600 x 600 window
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("BOUNCY BOUNCY!")

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
```

Now we have pygame, we have our screen but we need to start drawing something on the screen. Let's create a new class to draw the large circle that will contain our ball.


```python
class DrawCircle:
    def __init__(self):
        self.center = (300,300)
        self.radius = 255
        self.width = 3 

    def draw(self):
        pygame.draw.circle(screen,WHITE, self.center,self.radius,self.width)

```

Look how easy that was! We've now got a screen with a nice white circle around it. 

Now come's the tricky (but interesting!) part of this project. We need to make the ball bounce. 

Lets start by creating our BouncingBall class and initializing some variables 


```python
class BouncingBall:
    def __init__(self):
        self.x = 300
        self.y = 300
        self.velocity = [1, 2]
        self.radius = 15
        # Elasticity is the amount of energy the ball loses when it hits something
        self.elasticity = 0.9  
        # constant for gravity 
        self.gravity = 0.5  
```

Going through the variables,

The x and y coordinates will "spawn" our ball in the middle of the screen. 

The ball's velocity is represented as a list [1,2] and represents the speed and direction that the ball is currently moving in. The first value (1) is the initial horizontal speed (x-velocity) of the ball and the second value (2) is the initial vertical speed (y-velocity) of the ball. 

This means that the ball will start moving downwards and to the right. There's no specific reason for this apart from the fact that it give's it that nice arc as it bounces from left to right. 

Radius, how big the ball is. 

Elasticity is the amount of energy the ball is going to retain after it collides with the edge's of the outer-circle. An elasticity of 0.9 means that every time the ball collides it loses 10% of it's energy giving it a realistic bounce. 

And then we have a constant for gravity. Gravity acts as a constant downwards acceleration on the ball and makes the simulation look far more "real". 

Simple enough!

Now for the real fun part! Let's get this bad boy moving!

```python
    def move(self):
        # Apply gravity
        self.velocity[1] += self.gravity
        self.x += self.velocity[0]
        self.y += self.velocity[1]
```

Simple enough, we apply gravity to velocity of the y value (thus pulling it down a bit) and then move the x and y values of the ball depending on the ball's current in each of the directions. 

But currently we don't check at all for if the ball has hit the edge of the circle, so right now it's just going to move in one direction forever, let's change that and add some collision detection! (this is the real fun part)

In order to do this we are going to have to go back to high school and refresh our knowledge of **normal vectors**. 

```python



```









