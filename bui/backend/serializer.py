# -*- coding: utf-8 -*-
from bui.utils.parser import read_yaml
from elements import Fill
from layout import *

FRONTEND = 'pyopengl' # figure out where to stash this setting

if FRONTEND == 'blender':
    from bui.frontend.blender.elements import *

if FRONTEND == 'pyopengl':
    from bui.frontend.pyopengl.elements import *

def unserialize(document_container, root_structure=None):
    def construct_hierarchy(current_object, current_object_args, document_container):
        if 'children' in current_object_args:
            for child in current_object_args['children']:
                class_name = child.keys()[0]
                class_args = child.values()[0]
                
                if class_name == 'UIStructure':
                    document_name = class_args['name']
                    document_root = getattr(document_container, document_name)
                    structure = read_yaml(document_root)
                    root_object = structure.items()[0]
                    class_name = root_object[0]
                    class_args = root_object[1]
                
                class_instance = globals()[class_name](**class_args)
                current_object.append(class_instance)
                construct_hierarchy(class_instance, class_args, document_container)
    
    document_root = root_structure or document_container.root_structure
    structure = read_yaml(document_root)
    
    root_object_name = structure.keys()[0]
    root_object_args = structure.values()[0]
    root_object = globals()[root_object_name](**root_object_args)
    
    construct_hierarchy(root_object, root_object_args, document_container)
    
    return root_object
