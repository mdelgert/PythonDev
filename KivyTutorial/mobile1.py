#https://code.visualstudio.com/docs/python/python-tutorial
#https://medium.com/edureka/kivy-tutorial-9a0f02fe53f5

#msg = "Hello World"

#print(msg)

from kivy.app import App
from kivy.lang import Builder
 
from kivy.uix.boxlayout import BoxLayout
 
 
Builder.load_string('''
<Interface>:
    orientation: 'vertical'
    Button:
        text: 'Settings'
        font_size: 100
        on_release: app.open_settings()
''')
 
class Interface(BoxLayout):
    pass
 
class SettingsApp(App):
    def build(self):
        return Interface()
 
SettingsApp().run()