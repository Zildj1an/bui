from Blender import Draw

from bui.blender.application import BlenderApplication

# -------------------- UI STRUCTURE ----------------
ui_structure = '''
VerticalContainer:
    name: root_vertical
    width: 400
    children:
        - HorizontalContainer:
            name: test_hori
            children:
                - Label:
                    name: Test script
                - PushButton:
                    name: X
                    tooltip: Quit script
                    event_handler: quit_script
                    width: 20
        - Fill:
            height: 10
        - HorizontalContainer:
            name: last_hori
            children:
                - PushButton:
                    name: Do something
                    tooltip: Add some tool here
                    width: 100
                - Slider:
                    name: Test slider
        - HorizontalContainer:
            children:
                - Number:
                    name: Some number
                    value: 0.5
                - Number:
                    name: Another number
                - IntNumber:
                    name: Some int number
                    max: 100
'''

# ------------------------ HOTKEYS ---------------------
hotkeys = '''
d:
    press: d_was_pressed
    release: d_was_released
s: foobar
q: quit_script
'''

# ------------------------ EVENT HANDLERS --------------

def d_was_pressed(elem):
    print 'you pressed d!'

def d_was_released(elem):
    print 'you released d!'

def foobar(elem):
    print 'foobar'

def quit_script(elem):
    Draw.Exit()

# ----------------- INITIALIZATION -------------------
if __name__ == '__main__':
    app = BlenderApplication(ui_structure, hotkeys, globals())
    app.run()