import random
import robot_name


names = ["nathan", "bob"]

class Test(object):
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("hello world")

    def check_name(self):
        if self.name in names:
            self.say_hi()
        else:
            print("boo")

# b = Test("bob")
# b.check_name()
# print(Test().name)

# b = robot_name.Robot()
# print(b.name)
c = robot_name.Robot()
name1 = c.name
print(name1)
random.seed("Totally random.")
c.reset()
name2 = c.name
print(name2)
c.reset()
name3 = c.name
print(name3)