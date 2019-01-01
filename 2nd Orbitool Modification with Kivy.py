from kivy.config import Config 
Config.set('graphics', 'resizable', 0)
from kivy.core.window import Window
Window.size =(500, 650)
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button    
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
import math


root = Builder.load_string(""" 
<GridLayout>: 
    canvas.before:
        BorderImage:
            border: 10, 10, 10, 10
            source: 'C:/Users/Drew Ugbechie/Downloads/plain-backgrounds.jpg'
            pos: self.pos
            size: self.size

<FirstScreen>:    
    GridLayout:
        size_hint: 0.93, 0.93
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
            on_press: 
                root.manager.transition.duration = 0.5
                root.manager.current = "options_screen"
            size_hint: 2, 0.5
            pos_hint: {'center_x': 0.1, 'center_y': 0.1}
            font_size: '14sp'
            cols: 1
            rows: 1

<OptionsScreen>: 
    GridLayout:
        size_hint: 1, 0.9
        pos_hint: {'center_x': .5, 'center_y': .5}
        rows: 9
        cols: 3

        
    FloatLayout: 
        size_hint: (0.5, 0.2) 
        pos_hint: {'center_x': 0.5, 'center_y': 0.9}
        rows: 4 

        Label: 
            text: "Select element to compute."
            text_size: self.width-20, self.height-20 
            pos_hint: {'center_x': 0.52, 'center_y': 0.9}
            font_size: '16sp'

        Label:
            text: "Orbital Parameter Calculator. 2017."
            text_size: self.width-20, self.height-20 
            font_size: '13'


    FloatLayout: 
        size_hint: (0.5, 0.4) 
        rows: 7 
    
        Button: 
            text: "Semi-major Axis"
            on_press: 
                root.manager.transition.duration = 0.5
                root.manager.current = "smajor_screen"
            size_hint: (1, 0.25)
            pos_hint: {'center_x': 1, 'center_y': 2.0}
            font_size: '14sp'
            rows: 1
 

        Button: 
            text: "Semi-minor Axis"
            on_press: 
                root.manager.transition.duration = 0.5
                root.manager.current = "sminor_screen"
            size_hint: (1, 0.25)
            pos_hint: {'center_x': 1, 'center_y': 1.7}
            font_size: '14sp'
            rows: 1


        Button: 
            text: "Eccentricity"
            on_press: 
                root.manager.transition.duration = 0.5
                root.manager.current = "ecc_screen"
            size_hint: (1, 0.25)
            pos_hint: {'center_x': 1, 'center_y': 1.4}
            font_size: '14sp'
            rows: 1 

        Button: 
            text: "True Anomaly"
            on_press: 
                root.manager.transition.duration = 0.5
                root.manager.current = "trueano_screen"
            size_hint: (1, 0.25)
            pos_hint: {'center_x': 1, 'center_y': 1.1}
            font_size: '14sp'
            rows: 1


        Button: 
            text: "Apogee Radius"
            on_press: 
                root.manager.transition.duration = 0.5
                root.manager.current = "ar_screen"
            size_hint: (1, 0.25)
            pos_hint: {'center_x': 1, 'center_y': 0.8}
            font_size: '14sp'
            rows: 1

        Button: 
            text: "Perigee Radius"
            on_press: 
                root.manager.transition.duration = 0.5
                root.manager.current = "pr_screen"
            size_hint: (1, 0.25)
            pos_hint: {'center_x': 1, 'center_y': 0.5}
            font_size: '14sp'
            rows: 1

        Button: 
            text: "Quit"
            on_press: root.destroy
            size_hint: (0.3, 0.1)
            pos_hint: {'center_x': 1.8, 'center_y': 0.06}
            font_size: '14sp'
            rows: 1

<SemiMajorAxisScreen>: 
    id: calculator

    GridLayout:
        id: semimajor
        size_hint: 1, 0.9
        pos_hint: {'center_x': .5, 'center_y': .5}
        rows: 9
        cols: 3 

    FloatLayout: 
        size_hint: (0.5, 0.4) 
        rows: 7 
    
        Label: 
            text: "Apogee Radius (km) :"
            size_hint: (1, 0.25)
            pos_hint: {'center_x': 0.5, 'center_y': 2.0}
            font_size: '15sp'
            rows: 1

        TextInput: 
            id: entry1
            size_hint: (0.7, 0.25)
            pos_hint: {'center_x': 1.3, 'center_y': 2.0}
            font_size: '28sp'
            rows: 1

        Label: 
            text: "Perigee Radius (km) :"
            size_hint: (1, 0.25)
            pos_hint: {'center_x': 0.5, 'center_y': 1.6}
            font_size: '15sp'
            rows: 1

        TextInput: 
            id: entry2
            size_hint: (0.7, 0.25)
            pos_hint: {'center_x': 1.3, 'center_y': 1.6}
            font_size: '28sp'
            rows: 1 

        Button: 
            text: "Compute"
            on_press: 
                self.calculate
                entry3.text = self.calculate
            size_hint: (0.5, 0.15)
            pos_hint: {'center_x': 1.4, 'center_y': 1.3}
            font_size: '14sp'
            rows: 1 

        Label: 
            text: "The length of the Semi-Major Axis is,"
            size_hint: (1, 0.25)
            pos_hint: {'center_x': 0.7, 'center_y': 1}
            font_size: '15sp'
            rows: 1

        TextInput: 
            id: entry3
            size_hint: (0.3, 0.15)
            pos_hint: {'center_x': 1.4, 'center_y': 1}
            font_size: '20sp'
            rows: 1 

        Label: 
            text: "km."
            size_hint: (1, 0.25)
            pos_hint: {'center_x': 1.65, 'center_y': 1}
            font_size: '15sp'
            rows: 1

        Button: 
            text: "Clear Input"
            on_press: 
                entry1.text = ""
                entry2.text = ""
                entry3.text = ""
            size_hint: (1, 0.2)
            pos_hint: {'center_x': 1, 'center_y': 0.6}
            font_size: '14sp'
            rows: 1 

        Button: 
            text: "Back to Menu"
            on_press: 
                root.manager.transition.duration = 0.5
                root.manager.current = "options_screen"
            size_hint: (1, 0.2)
            pos_hint: {'center_x': 1, 'center_y': 0.3}
            font_size: '14sp'
            rows: 1 


        Label:
            text: "Orbital Parameter Calculator. 2017."
            text_size: self.width-20, self.height-20 
            font_size: '13'

""")


class FirstScreen(Screen):
    pass 
class OptionsScreen(Screen):
    pass 
class SemiMajorAxisScreen(Screen): 
    def calculate(self):
        a = float(entry1) 
        b = float(entry2) 
        c =  ((a + b)/ 2)
        
class SemiMinorAxisScreen(Screen): 
    pass
class EccentricityScreen(Screen):
    pass
class TrueAnomalyScreen(Screen):
    pass
class ApogeeRadiusScreen(Screen):
    pass
class PerigeeRadiusScreen(Screen):
    pass





sm = ScreenManager()
sm = ScreenManager(transition=FadeTransition())
sm.add_widget(FirstScreen(name= "first_screen"))
sm.add_widget(OptionsScreen(name= "options_screen"))
sm.add_widget(SemiMajorAxisScreen(name= "smajor_screen"))
sm.add_widget(SemiMinorAxisScreen(name= "sminor_screen"))
sm.add_widget(EccentricityScreen(name= "ecc_screen"))
sm.add_widget(TrueAnomalyScreen(name= "trueano_screen"))
sm.add_widget(ApogeeRadiusScreen(name= "ar_screen"))
sm.add_widget(PerigeeRadiusScreen(name= "pr_screen"))


class OrbitoolApp(App): 
    def build(self): 
        return sm   


               

if __name__ == '__main__': 
    OrbitoolApp().run()
