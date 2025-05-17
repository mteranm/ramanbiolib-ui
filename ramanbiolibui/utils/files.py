import os
import sys
import base64

def get_resource_path(relative_path):
    """ Get absolute path to a resource, works for dev and PyInstaller """
    if getattr(sys, 'frozen', False):  # Running as a PyInstaller bundle
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")  # Running normally

    return os.path.join(base_path, relative_path)

def image_to_base64(image_path):
    """ Convert an image to base64 encoding """
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')