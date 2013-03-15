"""
frame.py

(c) Charles Fracchia 2013
charlesfracchia@gmail.com

Permission granted for experimental and personal use;
license for commercial sale available from the author.

Frame class module

This class defines data and methods common to all devices. It is the base class for every type of device.
"""

class Frame(object):
    """docstring for Frame"""
    def __init__(self, arg):
        super(Frame, self).__init__()
        self.arg = arg
        