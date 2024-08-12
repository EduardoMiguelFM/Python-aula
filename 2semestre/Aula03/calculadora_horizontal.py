from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class Calculadora( App ):
    def build (self):

        superBox = BoxLayout(orientation="vertical")

        box = BoxLayout(orientation="horizontal")
        lbl_numero1 = Label(text="Digite o 1o número: ")
        txt_numero1 = TextInput()

        box.add_widget(lbl_numero1)
        box.add_widget(txt_numero1)
        

        bx = BoxLayout(orientation="vertical")
        lbl_numero2 = Label(text="Digite o 2o número: ")
        txt_numero2 = TextInput()

        bx.add_widget(lbl_numero2)
        bx.add_widget(txt_numero2)

        
        btn_somar = Button(text="Somar")
        bx.add_widget(btn_somar)

        superBox.add_widget(box)
        superBox.add_widget(bx)
        
        return superBox

obj_calculadora_soma = Calculadora()
obj_calculadora_soma.run()

