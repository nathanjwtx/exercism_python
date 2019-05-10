import random
import re

class Robot(object):
    def __init__(self):
        pass
    
    def name(self):
        alpha = (chr(random.randint(97, 123)) + chr(random.randint(97, 123))).upper()
        digits = random.randint(0, 1000)
        return alpha + str(digits)
        

