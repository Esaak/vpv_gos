import matplotlib.pyplot as plt
import pygame
from random import randint
colors = []


pygame.init()
def one_frame(planet, x,y, atmosphere, t):
    for i in range(len(atmosphere.w)):
        colors.append('#%06X' % randint(0, 0xFFFFFF))
    fig, ax = plt.subplots(figsize = (10, 10))
    for i in range(len(x)):
        ax.scatter(x[i], y[i], colors[i%len(colors)])
    circle1 = plt.Circle((0, 0), planet.R, color='r', fill= False)
    circle2 = plt.Circle((0, 0), atmosphere.height + planet.R, color='b', fill= False)
    ax.add_patch(circle1)
    ax.add_patch(circle2)
    ax.axis('equal')
    plt.savefig(f"pictures/graph_{t}.png")
    plt.show()

