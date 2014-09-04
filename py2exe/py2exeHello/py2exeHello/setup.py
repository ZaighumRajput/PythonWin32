from py2exe.build_exe import py2exe
from distutils.core import setup
import py2exe
import panda
import os
import zmq

os.environ["PATH"] = \
    os.environ["PATH"] + \
    os.path.pathsep + os.path.split(zmq.__file__)[0]

setup( console = [{"script": "py2exeHello.py"}],
        options={
                 "py2exe":{
                           "includes":
                           ["zmq.utils", "zmq.utils.jsonapi",
                            "zmq.utils.strtypes"]}})


