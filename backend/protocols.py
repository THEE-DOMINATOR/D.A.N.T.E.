# import listen
import think
import respond
import webview
from pathlib import Path
import subprocess
import platform

class GUI_API:
    def get_response(self):
        pass
    def get_thoughts(self):
        pass
    def take_input(self, input):
        pass

frontend_url = (Path(__file__).parent).parent / "frontend" / "index.html"
api = GUI_API()
print(frontend_url)
window = webview.create_window("D.A.N.T.E.", frontend_url.as_uri(), js_api=api)
print(str(Path(__file__).parent.parent/"assets"/"triangle_icon.png"))

if platform.system() == "Linux":
    webview.start(icon = str(Path(__file__).parent.parent/"assets"/"triangle_icon.png"))
elif platform.system() == "Windows":
    webview.start(icon = str(Path(__file__).parent.parent/"assets"/"triangle_icon.ico"))
elif platform.system() == "Darwin":
    webview.start()
    # sorry mac users, you dont get an icon! 
    # no seriously im on windows and cant get to a mac to generate an icns file, but i guess you can make it yourself from assets/triangle_icon.png
    # if you do, PLEASE make a pr :)

def start():
    pass