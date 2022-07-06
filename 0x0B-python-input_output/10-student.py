#!/usr/bin/python3
"""student to JSON"""


class Student:
    """a class"""

    def __init__(self, first_name, last_name, age):
        """constructor"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) == list and all(
                type(x) == str for x in attrs):
            return {x: getattr(self, x) for x in attrs if hasattr(self, x)}
        return self.__dict__
