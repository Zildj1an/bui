# -*- coding: utf-8 -*-
from Blender import Draw
from abstract import AbstractBlenderElement

class PushButton(AbstractBlenderElement):
    def render(self):
        Draw.PushButton(self.name, self.event, self.x, self.y,
                        self.width, self.height, self.tooltip)

class ToggleButton(AbstractBlenderElement):
    def initialize(self, **kvargs):
        self.value = False
        super(ToggleButton, self).initialize(**kvargs)
    
    def render(self):
        Draw.Toggle(self.name, self.event, self.x, self.y,
                    self.width, self.height, self.value, self.tooltip,
                    self.update_value)
