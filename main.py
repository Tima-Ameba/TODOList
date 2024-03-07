from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang.builder import Builder

Builder.load_file("main.kv")

class MainScreen(MDScreen):
    pass

class MyToDoList(MDApp):
    def build(self):
        return MainScreen()
    
if __name__== "__main__":
    MyToDoList().run()