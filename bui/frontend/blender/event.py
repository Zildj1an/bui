# -*- coding: utf-8 -*-
from Blender import Window
from Blender.Window import Types

from bui.backend.event import BaseEventManager

from keys import BLENDER_KEYS

class EventManager(BaseEventManager):
    def element_event(self, evt):
        super(EventManager, self).element_event(evt)
        
        Window.Redraw(Types.VIEW3D) # TODO: too specific?
        Window.Redraw(Types.SCRIPT)
    
    def construct_key_event_ids(self, hotkeys, key_mapping=None):
        super(EventManager, self).construct_key_event_ids(hotkeys, BLENDER_KEYS)
