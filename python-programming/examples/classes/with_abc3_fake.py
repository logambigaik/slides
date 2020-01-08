from with_abc3 import Base

class Fake(Base):
    def foo(self):
        print('foo in Fake')

f = Fake('Joe')

# Traceback (most recent call last):
#   File "with_abc3_fake.py", line 7, in <module>
#     f = Fake('Joe')
# TypeError: Can't instantiate abstract class Fake with abstract methods bar

