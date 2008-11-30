# -*- coding: utf-8 -*-
from Blender import Window

from bui.window import BaseWindowManager

class WindowManager(BaseWindowManager):
    def get_window_coords(self):
        win_id = Window.GetAreaID()
        win_data = Window.GetScreenInfo()
        
        for win in win_data:
            if win["id"] == win_id:
                return win["vertices"]
