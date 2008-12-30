# -*- coding: utf-8 -*-
from Blender import Draw

from abstract import AbstractBlenderElement

class Slider(AbstractBlenderElement):
    def __init__(self, **kvargs):
        self.value = 0.0
        super(Slider, self).__init__(**kvargs)
    
    def render(self):
        Draw.Slider(self.name + ': ', self.event, self.x, self.y,
                    self.width, self.height, self.value, self.min, self.max,
                    False, self.tooltip, self.update_value)
