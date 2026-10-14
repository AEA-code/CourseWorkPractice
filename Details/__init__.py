try:
    from .program import program
    from .duration import duration
    from .course import course
except ImportError:
    from program import program
    from duration import duration
    from course import course

__all__ = ["program", "duration", "course"]