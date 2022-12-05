import grpc

from flaui_pb2 import App, Coordinates, Empty, TypeRequest, By
from flaui_pb2_grpc import FlaRPCStub

import random
import string
from time import perf_counter

URL = "localhost:5001"


def get_credentials(cer_filename):
    with open(cer_filename, "rb") as f:
        return grpc.ssl_channel_credentials(f.read())


class FlaUIClient:
    def __init__(self, channel) -> None:
        self._stub = FlaRPCStub(channel)

    def launch(self, name):
        application = App(name=name)
        return self._stub.Launch(application).name

    def type(self, auto_id, text):
        by = By(automation_id=auto_id)
        type_req = TypeRequest(by=by, text=text)
        return self._stub.Type(type_req).text

    def click(self, by):
        return self._stub.Click(by)

    def click_by_coordinates(self, x, y):
        coords = Coordinates(x=x, y=y)
        return self._stub.ClickCoords(coords)
    
    def get_screenshot(self, filepath):
        file = self._stub.Screenshot(Empty())
        with open(filepath, 'wb') as f:
            f.write(file.buffer)


creds = get_credentials("dev_base64.cer")

with grpc.secure_channel(URL, credentials=creds) as channel:
    app_path = "C:\\Users\\msigs75\\VSCodeProjects\\flaui-grpc\\WpfApplication.exe"
    # app_path = "notepad.exe"

    client = FlaUIClient(channel)
    client.launch(app_path)

    s = ''.join([random.choice(string.ascii_letters) for _ in range(100)])
    client.type("TextBox", s)

    # client.click_by_coordinates(200, 250)
    client.click(By(name="ContextMenu"))

    client.get_screenshot('test_client_screenshot.jpg')
    client.get_screenshot('test_client_screenshot.png')
