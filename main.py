import tkinter as tk
class MyCalculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("550x650")
        self.root.title("ICON08")

        self.label = tk.Label(self.root, text="NISSANNN Calculator", font=('ariel', 40))
        self.label.pack()
        self.button = tk.Button(self.root, text="CE", font=('ariel', 25), width=3, height=1)
        self.button.place(x=85, y=150)
        self.button = tk.Button(self.root, text="()", font=('ariel', 25), width=3, height=1)
        self.button.place(x=185, y=150)
        self.button = tk.Button(self.root, text="%", font=('ariel', 25), width=3, height=1)
        self.button.place(x=285, y=150)
        self.button = tk.Button(self.root, text="/", font=('ariel', 25), width=3, height=1)
        self.button.place(x=385, y=150)
        self.button = tk.Button(self.root, text="x", font=('ariel', 25), width=3, height=1)
        self.button.place(x=385, y=240)
        self.button = tk.Button(self.root, text="-", font=('ariel', 25), width=3, height=1)
        self.button.place(x=385, y=340)
        self.button = tk.Button(self.root, text="+", font=('ariel', 25), width=3, height=1)
        self.button.place(x=385, y=440)
        self.button = tk.Button(self.root, text="7", font=('ariel', 25), width=3, height=1)
        self.button.place(x=85, y=240)
        self.button = tk.Button(self.root, text="8", font=('ariel', 25), width=3, height=1)
        self.button.place(x=185, y=240)
        self.button = tk.Button(self.root, text="9", font=('ariel', 25), width=3, height=1)
        self.button.place(x=285, y=240)
        self.button = tk.Button(self.root, text="4", font=('ariel', 25), width=3, height=1)
        self.button.place(x=85, y=340)
        self.button = tk.Button(self.root, text="5", font=('ariel', 25), width=3, height=1)
        self.button.place(x=185, y=340)
        self.button = tk.Button(self.root, text="6", font=('ariel', 25), width=3, height=1)
        self.button.place(x=285, y=340)
        self.button = tk.Button(self.root, text="1", font=('ariel', 25), width=3, height=1)
        self.button.place(x=85, y=440)
        self.button = tk.Button(self.root, text="2", font=('ariel', 25), width=3, height=1)
        self.button.place(x=185, y=440)
        self.button = tk.Button(self.root, text="3", font=('ariel', 25), width=3, height=1)
        self.button.place(x=285, y=440)
        self.button = tk.Button(self.root, text="+/-", font=('ariel', 25), width=3, height=1)
        self.button.place(x=85, y=540)
        self.button = tk.Button(self.root, text="0", font=('ariel', 25), width=3, height=1)
        self.button.place(x=185, y=540)
        self.button = tk.Button(self.root, text=".", font=('ariel', 25), width=3, height=1)
        self.button.place(x=285, y=540)
        self.button = tk.Button(self.root, text="=", font=('ariel', 25), width=3, height=1)
        self.button.place(x=385, y=540)
        self.label = tk.Label(self.root, text="", width=50, height=2).place(x=0, y=80) 


        self.root.mainloop()


MyCalculator()