from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class Calculadora(App):
    def build(self):
        box = BoxLayout(orientation='vertical')

        lbl_numero1 = Label(text="Diite o 1o número: ")
        txt_numero1 = TextInput()
        lbl_numero2 = Label(text="Digite o 2o número: ")
        txt_numero2 = TextInput()
        btn_somar = Button(text="Somar")

        box.add_widget(lbl_numero1)
        box.add_widget(txt_numero1)

        box.add_widget(lbl_numero2)
        box.add_widget(txt_numero2)

        box.add_widget(btn_somar)
        return box

obj_calculadora_soma = Calculadora()
obj_calculadora_soma.run()