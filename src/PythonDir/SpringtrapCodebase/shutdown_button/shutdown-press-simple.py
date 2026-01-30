#!/usr/bin/env python3

from gpiozero import Button

import os

Button(27).wait_for_press()

os.system("sudo shutdown -h now")
