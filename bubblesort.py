from pyglet.window import Window
from pyglet.app import run
from pyglet.shapes import Rectangle
from pyglet.graphics import Batch
from pyglet import clock
import math

class Renderer(Window):
    def __init__(self):
        super().__init__(640, 640, "Bubble Sort")
        self.batch = Batch()
        self.x = [3, 4, 2, 1, 5]
        self.bars = []
        for e, i in enumerate(self.x):
            self.bars.append(Rectangle(100 + e * 100, 100, 80, i * 100, color=(0, 0, 255), batch=self.batch))
        self.sorted = False
        self.i = 0
        self.j = 0
        self.done = False

    def on_update(self, deltatime):
        if not self.done:
            if self.i < len(self.x) - 1:
                if self.j < len(self.x) - self.i - 1:
                    if self.x[self.j] > self.x[self.j + 1]:
                        self.x[self.j], self.x[self.j + 1] = self.x[self.j + 1], self.x[self.j]
                        self.update_bars()
                    self.j += 1
                else:
                    self.j = 0
                    self.i += 1
            else:
                self.done = True

    def update_bars(self):
        self.batch = Batch()
        for e, i in enumerate(self.x):
            self.bars[e] = Rectangle(100 + e * 100, 100, 80, i * 100, color=(0, 0, 255), batch=self.batch)

    def on_draw(self):
        self.clear()
        self.batch.draw()

renderer = Renderer()
clock.schedule_interval(renderer.on_update, 0.2)
run()