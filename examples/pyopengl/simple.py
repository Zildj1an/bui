# -*- coding: utf-8 -*-
import os, sys

# FIXME: evilness!
bui_path = os.path.normpath(sys.path[0])
bui_path = bui_path[:bui_path.rfind('/')]
bui_path = bui_path[:bui_path.rfind('/')]
sys.path.append(bui_path)

from bui.frontend.pyopengl.window import WindowManager
from bui.utils.meta import AllMethodsStatic

# TODO: rename label "color" to label_color?

configuration = '''
    label: Simple layout test
    width: 640
    height: 480
    hotkeys: hotkeys
    structure: root_structure
    default_node_height: 20
    bg_color: [0.8, 0.8, 0.8]
'''

class UIStructure():
    root_structure = '''
    VerticalLayout:
        name: root_vertical
        bg_color: [0.2, 0.5, 0.6]
        width: auto
        children:
            - VerticalLayout:
                children:
                    - Label:
                        label: Some label
                    - Label:
                        label: Another label
                        alpha: 0.5 # test alpha
                    - Separator:
                        label: Test separator
                    - Label:
                        label: Hello world!
                        color: [0.1, 0.3, 0.1] # probably color: green would be nicer
            - HorizontalLayout:
                bg_color: [0.5, 0.8, 0.2]
                height: 200
                #width: 200 # if not set, uses auto layout (scales width to parent width)
                default_node_height: 30 # overrides default for children!
                children:
                    - Label:
                        label: First child
                        color: [0.0, 0.5, 0.0]
                        bg_color: [0.4, 0.9, 0.2]
                        #width: 100
                    - Label:
                        label: Second child
                        color: [0.0, 0.5, 0.0]
                        bg_color: [0.3, 0.8, 0.5]
                        #width: 200
    '''

class Hotkeys():
    hotkeys = '''
    d:
        press: d_was_pressed
        release: d_was_released
    s: foobar
    q: quit_script
    '''

class Events(AllMethodsStatic):
    def d_was_pressed(elem):
        print 'you pressed d!'
    
    def d_was_released(elem):
        print 'you released d!'
    
    def foobar(elem):
        print 'foobar'
    
    def quit_script(elem):
        sys.exit()

if __name__ == '__main__':
    window_manager = WindowManager(configuration, UIStructure, Hotkeys, Events)
    window_manager.run()
