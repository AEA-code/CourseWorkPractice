import os
import sys

if __package__ in (None, ""):
    project_root = os.path.dirname(os.path.dirname(__file__))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
    from Details.program import program
    from Details.course import course
    from Details.duration import duration
else:
    from .program import program
    from .course import course
    from .duration import duration

# create an object for program class
obj1 = program()
obj1.show()
print()
# create an object for course class
obj2 = course()
obj2.show()
print()
# create an object for duration class
obj3 = duration()
obj3.show()