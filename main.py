from kivymd.app import MDApp 
from kivymd.uix.screen import MDScreen
from kivy.lang.builder import Builder
from kivymd.uix.dialog import (
    MDDialog,
    MDDialogIcon,
    MDDialogHeadlineText,
    MDDialogSupportingText,
    MDDialogButtonContainer,
    MDDialogContentContainer,
)
from kivymd.uix.divider import MDDivider
from kivymd.uix.list import (
    MDListItem,
    MDListItemLeadingIcon,
    MDListItemSupportingText,
    MDListItemHeadlineText,
    MDListItemTrailingCheckbox
)
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.widget import Widget
Builder.load_file("main.kv")
import json

class MyContent(MDDialogContentContainer):
    pass

class MainScreen(MDScreen):
    def show_dialog(self):
        self.content=MyContent()
        self.dialog=MDDialog(
            # ----------------------------Icon-----------------------------
            MDDialogIcon(
                icon="book-plus-multiple-outline",
            ),
            # -----------------------Headline text-------------------------
            MDDialogHeadlineText(
                text="Добавить задачу",
            ),
            # -----------------------Custom content------------------------
            self.content,
            # ---------------------Button container------------------------
            MDDialogButtonContainer(
                Widget(),
                MDButton(
                    MDButtonText(text="Отмена"),
                    style="text",
                    on_release=lambda x: self.dialog.dismiss(),
                ),
                MDButton(
                    MDButtonText(text="Добавить"),
                    style="text",
                    on_release=lambda x:self.add()
                ),
                spacing="8dp",
            ),
            # -------------------------------------------------------------
        )
        self.dialog.open()
    def done_check(self,l):
        self.ids.list.remove_widget(l)
        self.ids.donelist.add_widget(l)
        
    def add(self):
        text1=self.content.ids.todotext.text
        text2=self.content.ids.todotext_two.text
        check=MDListItemTrailingCheckbox(
            )
        l=MDListItem(
            MDListItemHeadlineText(
                text=text1,
            ),
            MDListItemSupportingText(
                text=text2,
            ),
            check,
        )
        check.on_release=lambda x=l:self.done_check(x)
        l.radius=l.height//2
        self.ids.list.add_widget(l)
        self.dialog.dismiss()\
            
class MyToDoList(MDApp):
    def build(self):
        return MainScreen()
    
if __name__== "__main__":
    MyToDoList().run()