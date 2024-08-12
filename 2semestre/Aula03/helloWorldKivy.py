from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import button

class HelloWorld(App):
    def build (self):
        return Label(text="Hello World",
                      color="purple",
                      font_size="100")


HelloWorld().run()