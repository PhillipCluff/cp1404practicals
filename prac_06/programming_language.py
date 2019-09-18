""" class for programming languages """


class ProgrammingLanguage:
    """Represent a programming language object"""

    def __init__(self, name="", typing="", reflection="", year=0):

        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):

        return "{}, is a {} typing language that was established in {},its reflection is {}.".format(
            self.name, self.typing, self.year, self.reflection)

    def is_dynamic(self):
        return self.typing == "Dynamic"
