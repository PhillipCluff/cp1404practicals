"""
This program will Covert Miles to Kilometres with a nice GUI
It also has increment buttons
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

__author__ = 'Phillip Cluff'

# Just for clarity this number is how many kilometres in a mile.
MILES_TO_KILOMETRES = 1.60934


class MilesToKilometres(App):
    output = StringProperty()

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('miles_to_kilometres.kv')
        return self.root

    def handle_calculate(self, value_text):
        print("calculate started")
        result = self.convert_to_number(value_text) * MILES_TO_KILOMETRES
        self.output = str(result)

    def handle_increment(self, value_text, increment):
        new_number = self.convert_to_number(value_text) + increment
        self.root.ids.value_text.text = str(new_number)

    # a decorator is what this is called @ and staticmethod needs more research
    @staticmethod
    def convert_to_number(text):
        """Convert text to float or 0.0 if invalid."""
        try:
            value = float(text)
            return value
        except ValueError:
            return 0.0


MilesToKilometres().run()
