import grpc

from greet_pb2_grpc import GreeterStub
from greet_pb2 import HelloRequest
from flaui_pb2 import Application, TypeTextObject
from flaui_pb2_grpc import FlaRPCStub
from time import sleep

URL = "localhost:5001"


def get_credentials(cer_filename):
    with open(cer_filename, "rb") as f:
        return grpc.ssl_channel_credentials(f.read())


def say_hello(channel, name):
    stub = GreeterStub(channel)
    reply = stub.SayHello(HelloRequest(name=name))
    return reply.message


def launch_app(channel, name):
    application = Application(name=name)
    stub = FlaRPCStub(channel)
    return stub.Launch(application).name

def type_text(channel, element_id, text):
    stub = FlaRPCStub(channel)
    type_text_object = TypeTextObject(element=element_id, text=text)
    return stub.TestTypeText(type_text_object).text


creds = get_credentials("dev_base64.cer")

with grpc.secure_channel(URL, credentials=creds) as channel:
    print(launch_app(channel, "notepad.exe"))
    print(type_text(channel, "15", "absolutely random text"))
    # print(say_hello(channel, 'Python Client'))
