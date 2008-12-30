# -*- coding: utf-8 -*-
from Blender import Draw

from abstract import AbstractBlenderElement

class TextBox(AbstractBlenderElement):
    def __init__(self, **kvargs):
        self.value = ''
        super(TextBox, self).__init__(**kvargs)
    
    def render(self):
        Draw.String(self.name + ': ', self.event, self.x, self.y,
                    self.width, self.height, self.value, self.max_input_length,
                    self.tooltip, self.update_value)