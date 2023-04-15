from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
Window.size = (310, 580)

class Cindy(MDApp):

    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("welcome.kv"))
        #screen_manager.add_widget(Builder.load_file("login.kv"))
        return screen_manager
    
if __name__ == "__main__":
    LabelBase.register(name="MRoboto", fn_regular="D:\\Python Project\\Android\\Store_App\\Roboto\\font\\Roboto""-Medium.ttf")
    Cindy().run()