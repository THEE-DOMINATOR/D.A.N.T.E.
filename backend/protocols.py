import listen
import think
import respond
import webview
from pathlib import Path
import subprocess

class GUI_API:
    def get_response(self):
        pass
    def get_thoughts(self):
        pass
    def take_input(self, input):
        pass

frontend_url = Path(__file__).parent /"frontend"/"dist"/"index.html"
api = GUI_API()
window = webview.create_window(
    title = "D.A.N.T.E",
    url = frontend_url.as_uri(),
    js_api = api
)
webview.start()

def start():
    pass