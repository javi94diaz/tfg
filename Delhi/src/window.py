'''
Created on 5 mar. 2020

@author: Javier
'''

import ctypes
user32 = ctypes.windll.user32

SCREEN_WIDTH = user32.GetSystemMetrics(0)
SCREEN_HEIGHT = user32.GetSystemMetrics(1)

WIDTH_DIFF = 0
HEIGHT_DIFF = 110

WINDOW_WIDTH = SCREEN_WIDTH - WIDTH_DIFF
WINDOW_HEIGHT = SCREEN_WIDTH - HEIGHT_DIFF

X_COORDINATE = -7
Y_COORDINATE = 0