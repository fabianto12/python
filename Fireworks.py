import math
import random
import time
from turtle import *

setup(1000, 700)
speed(0)
tracer(0, 0)
bgcolor("#030305")

COLOR_PALETTES = [
    ["#ff0055", "#ff595e", "#ffca3a", "#ffffff", "#ff477e"],
    ["#00e5ff", "#0077b6", "#90e0ef", "#ffffff", "#48cae4"],
    ["#ffbe08", "#ff924c", "#ff595e", "#ffffff", "#faa307"],
    ["#8338ec", "#3a86ef", "#00f5d4", "#ffffff", "#9b5de5"],
    ["#70e000", "#38b000", "#ccff33", "#ffffff", "#9ef01a"],
    ["#ff007f", "#7209b7", "#4cc9f0", "#ffffff", "#f72585"]
]

class MegaFirework:
    def __init__(self):
        self.reset()

    def reset(self):
        
        self.x = random.randint(-400, 400)
        self.y = -350
        self.target_y = random.randint(0, 260)  
        self.speed = random.uniform(8, 14)       
        self.state = "launching"
        self.particles = []
        self.palette = random.choice(COLOR_PALETTES)

    def explode(self):
        self.state = "exploding"
        
        num_particles = random.randint(200, 300)
        
        for _ in range(num_particles):
            angle = random.uniform(0, 2 * math.pi)
            speed_p = random.uniform(2.0, 12.0)
            color_p = random.choice(self.palette)
            
            self.particles.append([
                self.x, self.y, 
                math.cos(angle) * speed_p, 
                math.sin(angle) * speed_p, 
                color_p, 
                random.randint(50, 90),  
                random.randint(4, 7)     
            ])

    def update(self):
        if self.state == "launching":
            self.y += self.speed
            penup()
            goto(self.x, self.y)
            pendown()
            color("#ffcc00")
            dot(6)  
            
            if self.y >= self.target_y:
                self.explode()

        elif self.state == "exploding":
            alive_particles = []
            for p in self.particles:
                p[0] += p[2]
                p[1] += p[3]
                p[2] *= 0.96
                p[3] *= 0.96
                p[3] -= 0.1  
                p[5] -= 1

                if p[5] > 0:
                    alive_particles.append(p)
                    penup()
                    goto(p[0], p[1])
                    pendown()
                    color(p[4])
                    dot(max(1, int(p[6] * (p[5] / 90))))

            self.particles = alive_particles
            if len(self.particles) == 0:
                self.reset()

fireworks = [MegaFirework() for _ in range(7)]

hideturtle()

try:
    while True:
        clear()
        for fw in fireworks:
            fw.update()
        update()
        time.sleep(0.01)
except TerminatedError:
    pass