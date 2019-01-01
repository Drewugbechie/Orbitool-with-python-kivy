from kivy.config import Config 
Config.set('graphics', 'resizable', 0)
from kivy.core.window import Window
Window.size =(500, 650)
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


root = Builder.load_string(""" 
<GridLayout>: 
    canvas.before:
        BorderImage:
            border: 10, 10, 10, 10
            source: 'C:/Users/Drew Ugbechie/Downloads/ENPA_Spray.jpg'
            pos: self.pos
            size: self.size

<RootWidget>:
    GridLayout:
        size_hint: 0.90, 0.90
        pos_hint: {'center_x': .5, 'center_y': .5}
        rows: 9
        cols: 3
        
        Label:
            text: "Payload Unit, Satellite System Division CSTD Abuja."
            text_size: self.width-20, self.height-20 
            font_size: '13'
            valign: 'top' 
            rows: 2

        Label: 
            text: "Ugbechie Andrew"
            font_size: '15sp'
            text_size: self.width-20, self.height-20
            valign: 'bottom'
            halign: 'right' 

        
    GridLayout: 
        size_hint: (0.4, 0.2) 
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        rows: 2 

        Label: 
            text: "ORBITOOL" 
            size_hint: 1, 1
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            font_size: '37sp'  
    
        Button: 
            text: "Click to Enter"
            # on_press: 
            #     root.manager.transition.direction = "left"
            #     root.manager.transition.duration = 1
            #     root.manager.current = "screen_two"
            size_hint: 2, 0.5
            pos_hint: {'center_x': 0.1, 'center_y': 0.1}
            font_size: '14sp'
            cols: 1
            rows: 1
""")


class RootWidget(FloatLayout): 
    pass
 
class OrbitoolApp(App): 
    def build(self): 
        return RootWidget()
if __name__ == '__main__': 
    OrbitoolApp().run()
