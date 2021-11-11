from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, StringProperty
from decimal import Decimal
from kivy.config import Config




Config.set('kivy', 'keyboard_mode', 'systemanddock')

class CalculateScreen(Screen):
    start_distance = ObjectProperty()
    finish_distance = ObjectProperty()
    start_gasoline = ObjectProperty()
    added_fuel = ObjectProperty()
    normal_consumption = ObjectProperty()
    
    def counting(self, start_distance, finish_distance, start_gasoline, added_fuel, normal_consumption):
        if self.added_fuel == 0:
            self.day_distance = str(finish_distance-start_distance)
            self.daily_consumption = str(Decimal(str((float(self.day_distance)*normal_consumption)/100)).quantize(Decimal("1.00")))
            #self.daily_consumption = str((float(self.day_distance)*normal_consumption)/100)
            self.gasoline_left = str(Decimal(str(start_gasoline-float(self.daily_consumption))).quantize(Decimal("1.00")))
            #self.gasoline_left = str(start_gasoline-float(self.daily_consumption))
        else:
            self.day_distance = str(finish_distance-start_distance)
            self.daily_consumption = str(Decimal(str((float(self.day_distance)*normal_consumption)/100)).quantize(Decimal("1.00")))
            #self.daily_consumption = str((float(self.day_distance)*normal_consumption)/100)
            self.gasoline_left = str(Decimal(str((start_gasoline+added_fuel)-float(self.daily_consumption))).quantize(Decimal("1.00")))
            #self.gasoline_left = str((start_gasoline+added_fuel)-float(self.daily_consumption))
            
        #return self.day_distance, self.daily_consumption, self.gasoline_left
        
    def calculations(self):        
        try:
            start_distance = float(self.start_distance.text)
        except:
            start_distance = 0
        try:
            finish_distance = float(self.finish_distance.text)
        except:
            finish_distance = 0
        try:
            added_fuel = float(self.added_fuel.text)
        except:
            added_fuel = 0
        try:
            normal_consumption = float(self.normal_consumption.text)
        except:
            normal_consumption = 0
        try:
            start_gasoline = float(self.start_gasoline.text)
        except:
            start_gasoline = 0
            
        
        self.counting(start_distance, finish_distance, start_gasoline, added_fuel, normal_consumption)
    
    def set_values(self):
        result_screen = self.manager.get_screen("result")
        result_screen.ids.day_distance_result.text = self.day_distance
        result_screen.daily_consumption_result.text = self.daily_consumption
        result_screen.gasoline_after_result.text = self.gasoline_left
        
        
class ResultScreen(Screen):
    day_distance_result = ObjectProperty()
    daily_consumption_result = ObjectProperty()
    gasoline_after_result = ObjectProperty()
    

class Manager(ScreenManager):
    screen_one = ObjectProperty(None)
    screen_two = ObjectProperty(None)
    

class MyApp(App):
    def build(self):
        m = Manager()
        return m

if __name__=='__main__':
    MyApp().run()
    



    
    