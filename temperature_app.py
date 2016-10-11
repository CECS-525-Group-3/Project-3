import random
import tkinter as tk


class Temperature(object):
    def __init__(self):
        self._temperature_value = 0
        self._observers = []

    def get_temperature(self):
        return _temperature_value

    def set_temperature(self, temperature):
        self._temperature_value = temperature
        for callback in self._observers:
            print('Temperature has Changed!')
            callback(self._temperature_value)

    def bind_to(self, callback):
        self._observers.append(callback)


class TemperatureFrame(tk.Frame):
    def __init__(self, temperature, master=None):
        super().__init__(master)
        self._create_text()
        temperature.bind_to(self._update_temperature)

    def _create_text(self):
        self.temperature_label = tk.Label(self.master, text=u'0\u2109', font=('Arial', 300))
        self.temperature_label.pack(side='top')

    def _update_temperature(self, temperature):
        self.temperature_label['text'] = u'{}\u2109'.format(temperature)
        self.master.update()


class Application(tk.Frame):
    def __init__(self, temperature, master=None):
        super().__init__(master)
        self.pack()
        self.init_frames(temperature)
        self.attach(temperature)
    
    def init_frames(self, temperature):
        self.temperature_frame = TemperatureFrame(temperature, self.master)
        self.temperature_frame.pack(side='top')
    
    def attach(self, temperature):
        while True:
            self.temperature_frame.after(1000, temperature.set_temperature(random.randint(50, 100)))

if __name__ == '__main__':
    root = tk.Tk()
    root.wm_title('Temperature Display')
    root.geometry('800x600')
    
    temperature = Temperature()

    app = Application(temperature, master=root)
    app.mainloop()
