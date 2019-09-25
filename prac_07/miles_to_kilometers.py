"""
This program will Covert Miles to Kilometres with a nice GUI
It also has increment buttons
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty

__author__ = 'Phillip Cluff'


class MilesToKilometers(App):
    output = StringProperty()

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('miles_to_kilometers.kv')
        return self.root

    def handle_calculate(self, value_text):
        result = float(value_text) * 1.60934
        self.output = str(result)

    # def handle_increment(self, value_text, increment):
    #     new_number = float(value_text) + increment
    #     self.update = str(new_number)


MilesToKilometers().run()
