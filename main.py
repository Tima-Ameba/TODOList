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

import json


Builder.load_file("main.kv")


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
        
        if not l.children[0].children[0].active:
            self.ids.donelist.remove_widget(l)
            self.ids.list.add_widget(l)
        else:
            self.ids.list.remove_widget(l)
            self.ids.donelist.add_widget(l)
        
    def add(self):
        text1=self.content.ids.todotext.text
        check= MDListItemTrailingCheckbox()
        l=MDListItem(
            MDListItemHeadlineText(
                text=text1,
            ),
           check,
        )
        check.on_release=lambda x=l:self.done_check(x)
        l.radius=l.height//2
        self.ids.list.add_widget(l)
        self.dialog.dismiss()

class MyToDoList(MDApp):
    def on_stop(self):
        file={}
        for i in self.mainwindow.ids.list.children:
            text=i.children[1].children[0].children[0].text
            check=i.children[0].children[0].active
            file[text]=int(check)
        for i in self.mainwindow.ids.donelist.children:
            text=i.children[1].children[0].children[0].text
            check=i.children[0].children[0].active
            file[text]=int(check)
        with open("todo.json","w") as f:
            f.write(json.dumps(file))
    def build(self):
        self.mainwindow=MainScreen()
        try:
            with open("todo.json", "+a",encoding='utf-8') as f:
                todolist=json.load(f)
                for i in todolist:
                    text1=i
                    check= MDListItemTrailingCheckbox(active=bool(todolist[i]))
                    l=MDListItem(
                        MDListItemHeadlineText(
                            text=text1,
                        ),
                    check,
                    )
                    check.on_release=lambda x=l:self.mainwindow.done_check(x)
                    l.radius=l.height//2
                    if check.active:
                        self.mainwindow.ids.donelist.add_widget(l)
                    else:
                        self.mainwindow.ids.list.add_widget(l)
            
        
        except:
            pass
        return self.mainwindow
       
if __name__== "__main__":
    MyToDoList().run()