bl_info = {
    "name": "Tools:Q",
    "author": "studioQ",
    "version": (1, 0, 0),
    "blender": (2, 93, 3),
    "description": "Tools:Q Animation",
    "warning": "",
    "support": "COMMUNITY",
    "wiki_url": "",
    "category": "Animation"
}

import importlib
import os


IGNORE_DIR_LIST = [
    ".git",
    "__pycache__",
]


def get_funcs(func_name):
    this_path = os.path.dirname(__file__)
    dir_list = [
        f for f in os.listdir(this_path)
        if os.path.isdir(os.path.join(this_path, f)) and (f not in IGNORE_DIR_LIST)
    ]
    path_list = ["." + f for f in dir_list]

    functions = []
    for path in path_list:
        module = importlib.import_module(path, package=__package__)
        if hasattr(module, func_name):
            functions += [getattr(module, func_name)]
        
    return functions


def register():
    # Register Packages
    for func in get_funcs("register_package"):
        func()


def unregister():
    # Unregister Packages
    for func in get_funcs("unregister_package"):
        func()


if __name__ == "__main__":
    register()
