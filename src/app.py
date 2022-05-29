import kivy
kivy.require('2.1.0') # replace with your current kivy version !

# widgets
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

# UI
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.pagelayout import PageLayout

# graphics
from kivy.graphics import Color, Rectangle

class Card(GridLayout):
    def __init__(self, **kwargs) -> None:
        super(Card, self).__init__(**kwargs)
        self.cols = 3
        self.add_widget(Label(
            text='[color=00ff00][b]Points[/b][/color]', 
            markup=True, 
            width=0.2, 
            font_size=16,
            halign='left',
            valign='top'))
        self.add_widget(Label(
            text='[color=00ff00][b]Keyword(s)[/b][/color]', 
            markup=True, 
            width=0.4, 
            font_size=16,
            halign='left',
            valign='top'))
        self.add_widget(Label(
            text='[color=00ff00][b]Definition[/b][/color]', 
            markup=True, 
            width=0.4,
            font_size=16,
            halign='left',
            valign='top'))

class LevelUp(App):
    def __init__(self, **kwargs) -> None:
        super(LevelUp, self).__init__(**kwargs)
        self.window = BoxLayout(orientation='vertical')

    def build(self):
        # return Card()
        self.window.add_widget(Card())
        true_btn = Button(text='TRUE', font_size=20)
        false_btn = Button(text='FALSE', font_size=20)
        self.window.add_widget(true_btn)
        self.window.add_widget(false_btn)
        return self.window

if __name__ == '__main__':
    app = LevelUp()
    app.run()
