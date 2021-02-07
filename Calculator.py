from kivy.app import App
from kivy.uix.widget import Widget

class MyGridLayout(Widget):
    pass


class CalculatorApp(App):
    def build(self):
        return MyGridLayout()

if __name__=="__main__":
    calculator=CalculatorApp()
    calculator.run()