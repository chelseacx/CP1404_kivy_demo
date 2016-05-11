from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
Window.size = (900, 400)

class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        if self.root.ids.input_name.text != "":
            self.root.ids.output_label.text = "Hello " + self.root.ids.input_name.text

    def reset(self):
        self.root.ids.output_label.text = "Enter your name"
        self.root.ids.input_name.text = ""


BoxLayoutDemo().run()
