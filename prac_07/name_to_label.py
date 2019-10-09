"""
This make a list of names and make each name a label
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

name_to_display = ['jill', 'frank', 'ron']


class NameToLabelApp(App):

    def build(self):
        self.title = "Names to Labels"
        self.root = Builder.load_file('name_to_label.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in name_to_display:
            name_label = Label(text=name)
            self.root.ids.label_box.add_widget(name_label)


NameToLabelApp().run()
