import sys

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import  GridLayout
from kivy.uix.stacklayout import  StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import StringProperty
from kivy.graphics.vertex_instructions import Line
from kivy.graphics.context_instructions import Color
from kivy.uix.label import  Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.config import Config


class mainApp(App):
  def build(self):
      self.operator =["-","+","/","*"]
      main_layout=BoxLayout(orientation="vertical")
      self.solution =TextInput()
      main_layout.add_widget(self.solution)
      buttons=[["1","2","3","/"],["4","5","6 " ,"*"],["7","8","9","+"],["0",".","#","-"]]
      for row in buttons:
          h_layout=BoxLayout(orientation="horizontal")
          for label in row:
              but=Button(text=label)
              h_layout.add_widget(but)
              but.bind(on_press=self._press)
          main_layout.add_widget(h_layout)

      return main_layout
  def _press(self,source):
      current=self.solution
      clic=source.text


mainApp().run()