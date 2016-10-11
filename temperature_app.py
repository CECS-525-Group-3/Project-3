import tkinter as tk


class TemperatureFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self._create_text()

    def _create_text(self):
        self.temperature_label = tk.Label(self.master, text=u'0\u2109', font=('Arial', 300))
        self.temperature_label.pack(side='top')
        

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.init_frames()

    def init_frames(self):
        self.temperature_frame = TemperatureFrame(self.master)
        self.temperature_frame.pack(side='top')

if __name__ == '__main__':
    root = tk.Tk()
    root.wm_title('Temperature Display')
    root.geometry('800x600')
    
    app = Application(master=root)
    app.mainloop()

