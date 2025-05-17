import os
import sys
import base64
import pkg_resources

def get_resource_path(relative_path):
    """ Get absolute path to a resource, works for dev and PyInstaller """
    if getattr(sys, 'frozen', False):  # Running as a PyInstaller bundle
        return os.path.join(sys._MEIPASS, relative_path)
    return pkg_resources.resource_filename(__name__, relative_path).replace("/ramanbiolibui/utils", "")

def image_to_base64(image_path):
    """ Convert an image to base64 encoding """
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')