"""
Class example.

??
"""


class A():
    """A class."""

    num = 0

    def __init__(self, number):
        """Init method."""
        self.num = number

    def print_num(self):
        """Print number."""
        print(self.num)


class B(A):
    """B class."""

    name = ""

    def __init__(self, number, name):
        """Init method."""
        A.__init__(self, number)
        self.name = name

    def print_all(self):
        """Print all."""
        A.print_num(self)
        print(self.name)

object_b = B(123, "asdf")
object_b.print_all()
