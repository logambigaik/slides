from with_abc3 import Base

b = Base('Boss')

# Traceback (most recent call last):
#   File "with_abc3_base.py", line 3, in <module>
#     b = Base('Boss')
# TypeError: Can't instantiate abstract class Base with abstract methods bar, foo
