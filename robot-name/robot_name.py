import random
names = []


class Robot(object):

    def __init__(self):
        self.name = self.make_name()

    def make_name(self):
        while True:
            alpha = (chr(random.randint(97, 123)) + chr(random.randint(97, 123))).upper()
            digits = random.randint(100, 1000)
            new_name = alpha + str(digits)

            if new_name not in names:
                names.append(new_name)
                return new_name
            else:
                self.reset()

    def reset(self):
        self.name = self.make_name()
