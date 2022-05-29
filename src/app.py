import numpy as np
import pandas as pd
import random
import kivy
kivy.require('2.1.0') # replace with your current kivy version !

# widgets
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooser, FileChooserIconLayout

# UI
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelHeader, TabbedPanelItem, TabbedPanelStrip

# graphics
from kivy.graphics import Color, Rectangle

# GLOBALS
card_deck = pd.DataFrame(data=np.empty(shape=(0,3),))
sample_deck = list([
    ('synthesis', 'The creationo of\nsomething from\ndifferent elements.'),
    ('symbiosis', 'Win-win relationship\nbetween two species.'),
    ('exoplanet', 'Planet from outside\nthe solar system.'),
    ('force', 'The ability\nto do work.'),
    ('combustion', 'Chemical reaction\nthat uses oxygen and produces\ncarbon dioxide.'),
    ('distribution', 'Function that maps\nvalues in a valid\nrange to a\nprobability measure.'),
])

class Card(GridLayout):
    def __init__(self, cols: int, **kwargs) -> None:
        super(Card, self).__init__(**kwargs)
        self.cols = cols

class LevelUp(App):
    def __init__(self, **kwargs) -> None:
        super(LevelUp, self).__init__(**kwargs)
        self.window = BoxLayout(orientation='vertical')

    def build(self):
        # page for learning
        tp = TabbedPanel()
        th1 = TabbedPanelHeader(text='Learn', size_hint=(0.3, 0.1))
        tp.add_widget(th1)

        ti1 = BoxLayout(orientation='vertical')
        curr_card = Card(cols=3)

        if card_deck.size == 0:
            content = BoxLayout(orientation='vertical')
            content.add_widget(Label(text='Card deck is empty.\nAdd new cards or import from CSV on "Add" tab.'))
            ok_btn = Button(text='OK', font_size=12, size_hint=(0.5, 0.1))
            content.add_widget(ok_btn)
            card_deck_empty_popup = Popup(title='Alert',
                  content=content,
                  size_hint=(None, None), size=(400, 400))

            ok_btn.bind(on_press=card_deck_empty_popup.dismiss)
            card_deck_empty_popup.open()
            # card_deck_empty_popup.dismiss()

            # sample cards
            curr_card.add_widget(Label(
                text=f'[color=00ff00][b]{random.randrange(10, 100)}[/b][/color]',
                markup=True,
                font_size=16,
                halign='left',
                valign='top'))
            
            global sample_deck
            two_slice = random.choice(sample_deck)
            curr_card.add_widget(Label(
                text=f'[color=00ff00][b]{two_slice[0]}[/b][/color]',
                markup=True,
                font_size=16,
                size_hint_y=None,
                halign='left',
                valign='top'))

            curr_card.add_widget(Label(
                text=f'[color=00ff00][b]{two_slice[1]}[/b][/color]',
                markup=True,
                font_size=16,
                size_hint_y=None,
                halign='left',
                valign='top'))

        else:
            card = random.choice(card_deck)
            for i in range(3):
                curr_card.add_widget(Label(
                    text=f'[color=00ff00][b]{card[i]}[/b][/color]',
                    markup=True,
                    font_size=16,
                    halign='left',
                    valign='top'))

        # category buttons
        keep_btn = Button(text='Keep', font_size=20)
        keep_briefly_btn = Button(text='Keep Briefly', font_size=20)
        pass_btn = Button(text='Pass', font_size=20)

        
        def next_card_cb(param):
            curr_card.clear_widgets()
            
            # sample cards
            curr_card.add_widget(Label(
                text=f'[color=00ff00][b]{random.randrange(10, 100)}[/b][/color]',
                markup=True,
                font_size=16,
                halign='left',
                valign='top'))

            global sample_deck
            two_slice = random.choice(sample_deck)
            curr_card.add_widget(Label(
                text=f'[color=00ff00][b]{two_slice[0]}[/b][/color]',
                markup=True,
                font_size=16,
                size_hint_y=None,
                halign='left',
                valign='top'))

            curr_card.add_widget(Label(
                text=f'[color=00ff00][b]{two_slice[1]}[/b][/color]',
                markup=True,
                font_size=16,
                size_hint_y=None,
                halign='left',
                valign='top'))

            button_card = Card(cols=3)
            for btn in list([keep_btn, keep_briefly_btn, pass_btn]):
                btn.bind(on_press=next_card_cb)
                curr_card.add_widget(btn)

        button_card = Card(cols=3)
        for btn in list([keep_btn, keep_briefly_btn, pass_btn]):
            btn.bind(on_press=next_card_cb)
            curr_card.add_widget(btn)

        ti1.add_widget(curr_card)
        ti1.add_widget(button_card)
        th1.content = ti1

        # page for adding cards        
        th2 = TabbedPanelHeader(text='Add', size_hint=(0.3, 0.1))
        tp.add_widget(th2)
        ti2 = BoxLayout(orientation='vertical')

        # card section labels
        add_card = Card(cols=3)
        for text in list([
            '[color=aa00ff][b]Number of points:[/b][/color]',
            '[color=aa00ff][b]Keyword(s):[/b][/color]',
            '[color=aa00ff][b]Definition:[/b][/color]',
        ]):
            add_card.add_widget(Label(
                    text=text,
                    markup=True,
                    font_size=16,
                    halign='left',
                    valign='top'))

        # card section inputs
        for _ in range(3):
            add_card.add_widget(TextInput(multiline=False))

        def add_btn_cb():
            global card_deck
            card_deck = card_deck.append(other=pd.Series(data=list([add_card.children[i] for i in range(3)])))
            print(card_deck.head())

        add_btn = Button(text='Add', font_size=20)
        add_btn.bind(on_press=add_btn_cb)
        
        def import_btn_cb(mouse):
            file_chooser = FileChooser(multiselect=False)
            # card_deck = pd.read_csv(filepath_or_buffer='')

        import_btn = Button(text='Import', font_size=20)
        import_btn.bind(on_press=import_btn_cb)

        ti2.add_widget(add_card)
        ti2.add_widget(add_btn)
        ti2.add_widget(import_btn)
        th2.content = ti2
        tp_strip = TabbedPanelStrip(tabbed_panel=tp)

        self.window.add_widget(tp)
        self.window.add_widget(tp_strip)
        return self.window

if __name__ == '__main__':
    app = LevelUp()
    app.run()
