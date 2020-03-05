'''
Created on 5 mar. 2020

@author: Javier
'''

import window
import tkinter as tk
from tkinter import ttk

class HomeFrame(ttk.Frame):     #MANAGER PACK
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.portada = tk.PhotoImage (file = "portada.png")        
        self.image_label = ttk.Label(self, image = self.portada).pack(side = 'top')

class SolveFrame(ttk.Frame):    #MANAGER GRID
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.label1 = ttk.Label(self, text = "Label 1")
        self.label1.grid(row = 0, column = 0, padx=30, pady=30)
        
        self.label2 = ttk.Label(self, text = "Label 2")
        self.label2.grid(row = 1, column = 0)
        
        self.help_button = ttk.Button(self, text="Show Help", command =self.show_help)
        self.help_button.grid(row = 2, column = 0)
        
        self.equation1_entry = ttk.Entry(self, width = 25)
        self.equation1_entry.grid(row = 0, column = 1)
        self.equation1_entry.insert(0, "Type your fist equation here")
        
        self.equation2_entry = ttk.Entry(self, width = 25)
        self.equation2_entry.grid(row = 1, column = 1)
        self.equation2_entry.insert(0, "Type your second equation here")
        
        self.help_label = ttk.Label(self)
        self.help_label.grid(row = 2, column = 1)
        
       # self.solution = ttk.Label(self, text = "Label 2")
       # self.solution.pack()
        
    def show_help(self):
        if (self.help_label["text"] == ""):
            self.help_label["text"] = ("Press this button to hide this.")
        else: self.help_label["text"] = ""

class ModulesFrame(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
            

class Application(ttk.Frame):   #MANAGER GRID
    
    def __init__(self, root):
        super().__init__(root)
        root.title("DELHI")        
        
        root.geometry("{}x{}+{}+{}".format(
            window.WINDOW_WIDTH, 
            window.WINDOW_HEIGHT, 
            window.X_COORDINATE, 
            window.Y_COORDINATE))
        root.resizable(True, True)
        
        #Ahora el notebook para tener pestañas     
        self.notebook = ttk.Notebook(
            self, width = window.WINDOW_WIDTH -25, height = window.WINDOW_HEIGHT -45)
        
        self.home_frame = HomeFrame(self.notebook)
        self.notebook.add(
                self.home_frame, text="Home", padding=10)
        
        self.solver_frame = SolveFrame(self.notebook)
        self.notebook.add(
                self.solver_frame, text="Solver", padding=10)
        
        self.mod1_frame = ModulesFrame(self.notebook)
        self.notebook.add(
            self.mod1_frame, text="Module 1", padding=10)
        
        self.mod2_frame = ModulesFrame(self.notebook)
        self.notebook.add(
            self.mod2_frame, text="Module 2", padding=10)
        
        self.mod3_frame = ModulesFrame(self.notebook)
        self.notebook.add(
            self.mod3_frame, text="Module 3", padding=10)
        
        self.notebook.grid(row = 0, column = 0, padx=10, pady=10)
        self.grid(row=0, column = 0)
        