#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.grid import SmartTileWithLabel

from utils import get_data
# from main import get_bumps

from kivy.uix.gridlayout import GridLayout
# from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import NumericProperty
from kivy.clock import Clock

# Builder.load_string('''
# <GridLayout>:
#     cols: 2
#     Button:
#         text: 'Bumps'
#         background_color : [0,1,0,1]
# ''')

global bump

Builder.load_string("""
<startcountScreen>
    name: 'startcount'
    bumplabel: bumplabel
    MDSpinner:
        id: spinner
        active: False
        size_hint: None, None
        size: dp(46), dp(46)
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    ScrollView:
        do_scroll_x: False
        GridLayout:
            rows: 2
            Label:
                id: bumplabel
                text: ''  
                font_size: 100
                color: [0, 0, 0, 1]
            Button:
                text: "Update bump"
                font_size: '30dp'
                text_size: self.width - 50, self.height
                on_press: root.fc()
""")


# class startcountScreen(Screen):
#     def on_enter(self):
#         # sponsors = get_data('sponsors')
#         grid = self.ids.startcount_grid
#         color = [0.64, 0.84, 0.98, 0.5]
#         # for sponsor in sponsors:
#         #     grid.add_widget(SmartTileWithLabel(mipmap=True, keep_ratio=True,
#         #                                        box_color=color, overlap=False,
#         #                                        text=sponsor['name'],
#         #                                        source=sponsor['logo']))
#         self.ids.spinner.active = False
def update_bumps(bumpscounter):
    global bump
    bump = bumpscounter
    startcountScreen2 = startcountScreen()
    startcountScreen2.fc()
    # return bump

class startcountScreen(Screen):
    # def on_enter(self):
    # bump2 = NumericProperty(0)
    # bumplabel.text = str(bump) 
    
    def fc(self):
        global bump
        # bump2 = get_bumps()
        self.ids.bumplabel.text = str(bump)
    
    def build(self):
        
        # layout = startcountScreen(cols=2) 
        # layout.add_widget(Button(text='Widget 1'))
        # print("bump", bump)
        self.ids.spinner.active = False
        # self.ids.bumplabel.text = str(bump)
        # self.score_label.text = str(self.score)
        return startcountScreen



# class oneWidgetApp(App):
#     def build(self):
#         layout = GridLayout(cols=2)
#         layout.add_widget(Button(text='Widget 1'))
#         return layout
# if __name__ == '__main__':
#     oneWidgetApp().run()