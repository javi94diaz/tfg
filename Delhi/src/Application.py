'''
Created on 5 mar. 2020

@author: Javier
'''

import window
import tkinter as tk
from tkinter import ttk

class FileFrame(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.new_icon = tk.PhotoImage (file = "newicon.png")        
        self.new_label = ttk.Label(self, image = self.new_icon, text = "NEW").grid(row = 0, column = 0)

class EditFrame(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
#         self.label1 = ttk.Label(self, text = "Label 1")
#         self.label1.grid(row = 0, column = 0, padx=30, pady=30)
#         
#         self.label2 = ttk.Label(self, text = "Label 2")
#         self.label2.grid(row = 1, column = 0)
#         
#         self.help_button = ttk.Button(self, text="Show Help", command =self.show_help)
#         self.help_button.grid(row = 2, column = 0)
#         
#         self.equation1_entry = ttk.Entry(self, width = 25)
#         self.equation1_entry.grid(row = 0, column = 1)
#         self.equation1_entry.insert(0, "Type your fist equation here")
#         
#         self.equation2_entry = ttk.Entry(self, width = 25)
#         self.equation2_entry.grid(row = 1, column = 1)
#         self.equation2_entry.insert(0, "Type your second equation here")
#         
#         self.help_label = ttk.Label(self)
#         self.help_label.grid(row = 2, column = 1)
        
        # self.solution = ttk.Label(self, text = "Label 2")
        # self.solution.pack()
        
#     def show_help(self):
#         if (self.help_label["text"] == ""):
#             self.help_label["text"] = ("Press this button to hide this.")
#         else: self.help_label["text"] = ""

class HelpFrame(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
            
class SolverFrame(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Application(ttk.Frame):
    
    def __init__(self, root):
        super().__init__(root)
        root.title("DELHI")
        
        self.notebook = ttk.Notebook(
            self, width = 400, height = 100) #window.WINDOW_HEIGHT -45 de alto, window.WINDOW_WIDTH -25 de ancho
        
        self.new_icon = tk.PhotoImage (file = "newicon.png")
        self.new_tab_img = tk.PhotoImage (file = "newlabel.png")
        
        self.file_frame = FileFrame(self.notebook)
        self.notebook.add(
                self.file_frame, text = "File", padding=10) #, image = self.new_tab_img
        
        self.edit_frame = EditFrame(self.notebook)
        self.notebook.add(
                self.edit_frame, text="Edit", padding=10)
        
        self.help_frame = HelpFrame(self.notebook)
        self.notebook.add(
            self.help_frame, text="Help", padding=10)
        
        s = ttk.Style()
        s.configure('LateralMenu.TFrame', background = 'lightorange')
        s.configure('SolverFrame.TFrame', background = 'dodgerblue')
        s.configure('tools.TFrame', background = "lightblue")
        
        self.lateral_menu = ttk.Frame(self, width = 100, height = 426, style = 'LateralMenu.TFrame')
        self.solver_frame = ttk.Frame(self, width = 300, height = 300, style = 'SolverFrame.TFrame')
        
        self.lateral_menu.grid(row = 0, column = 0, rowspan = 2, sticky = "NSWE")
        self.notebook.grid(row = 0, column = 1, sticky = "NSWE")
        self.solver_frame.grid(row = 1, column = 1, sticky = "NSWE")
        self.grid(row=0, column = 0)
        
    def toggleFullScreen(self, event):
        root.fullScreenState = not root.fullScreenState
        root.window.attributes("-fullscreeen", root.fullScreenState)
        
    def quitFullScreen(self, event):
        root.fullScreenState = False
        root.window.attributes("-fullscreeen", root.fullScreenState)
        
        
        
        
        
        