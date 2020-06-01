'''
Created on 5 mar. 2020

@author: Javier
'''

from tkinter import *
from tkinter import ttk
import Application
from sympy import *
import sympy as sp

def show_welcome():
    solver.grid_remove()
    stepbystep.grid_remove()
    testbench.grid_remove()
    welcome.grid(column=0, row=0, sticky = "nsew")

def show_solver():
    welcome.grid_remove()
    stepbystep.grid_remove()
    testbench.grid_remove()
    solver.grid(column=0, row=0, sticky = "nsew")
    
def show_stepbystep():
    solver.grid_remove()
    welcome.grid_remove()
    testbench.grid_remove()
    stepbystep.grid(column=0, row=0, sticky = "nsew")
    
def show_testbench():
    solver.grid_remove()
    welcome.grid_remove()
    stepbystep.grid_remove()
    testbench.grid(column=0, row=0, sticky = "nsew")
    
if __name__ == '__main__':
    
    root = Tk()
    root.title("DELHI Solver")
#     app = Application.Application(root)
#     app.mainloop()
    s = ttk.Style()
    s.configure('lateral.TFrame', background='lightblue')
    s.configure('solver.TFrame', background="dodgerblue")
    s.configure('welcome.TFrame', background="orange")
    s.configure('stepbystep.TFrame', background="lightgreen")
    s.configure('testbench.TFrame', background="salmon")
    
    content = ttk.Frame(root)
    lateral = ttk.Frame(content, relief ="sunken", width=100, height=400, style="lateral.TFrame")
    notebook = ttk.Frame(content, relief ="sunken", width=500, height=100)
    workarea = ttk.Frame(content, relief ="sunken", width=500, height=300)
    solver = ttk.Frame(workarea, width=500, height=300, style="solver.TFrame")
    welcome = ttk.Frame(workarea, width=500, height=300, style="welcome.TFrame")
    stepbystep = ttk.Frame(workarea, width=500, height=300, style="stepbystep.TFrame")
    testbench = ttk.Frame(workarea, width=500, height=300, style="testbench.TFrame")
    
    cover =  PhotoImage (file = "images/cover.png")
    coverlbl = ttk.Label(welcome, image=cover).pack()
    
    cmdhistory = ttk.Label(solver, text= "Here is shown your command history", padding = 10)
    cmdentry = ttk.Entry (solver, text= "Type here...")
    plotter = ttk.Notebook(solver, width = 200, height = 250, padding = 10)
    equationplot = ttk.Frame(plotter)
    solutionplot= ttk.Frame(plotter)
    plotter.add(equationplot, text = "Equation", padding = 5)
    plotter.add(solutionplot, text  = "Solution", padding =  5)
    solutionlbl = ttk.Label(solver, text = "Solution expression in LaTex")
    
    cmdhistory.grid(column=0, row=0, sticky="nsew")
    cmdentry.grid(column=0, row=1, sticky="nsew")
    plotter.grid(column=1, row=0, sticky="nsew")
    solutionlbl.grid(column=1, row=1, sticky="nsew")
    
    etsiiupmicon = PhotoImage (file = "images/etsii.png")
    etsiilbl = ttk.Label(lateral, image = etsiiupmicon)
    etsiilbl.pack(side = TOP, expand = False)
    workoptions = ttk.Frame(lateral, relief = "sunken", width=80, height = 200)
    workoptions.pack(side = TOP, expand = True, fill = BOTH)
    welcomebtn = ttk.Button(workoptions, text = " Welcome ", command = show_welcome)
    solverbtn = ttk.Button(workoptions, text = " Solver ", command = show_solver)
    stepsbtn = ttk.Button(workoptions, text = " Step-by-step ", command = show_stepbystep)
    testbenchbtn = ttk.Button(workoptions, text = "Testbench", command = show_testbench)
    welcomebtn.pack(side = TOP, expand = True, fill = BOTH)
    solverbtn.pack(side = TOP, expand = True, fill = BOTH)
    stepsbtn.pack(side = TOP, expand = True, fill = BOTH)
    testbenchbtn.pack(side = TOP, expand = True, fill = BOTH)
    
    cuaderno = ttk.Notebook(notebook, width = 300, height = 50)
    page1 = ttk.Frame(cuaderno)
    page2 = ttk.Frame(cuaderno)
    page3 = ttk.Frame(cuaderno)
    cuaderno.add(page1, text=" File ", padding=5)
    cuaderno.add(page2, text=" Edit ", padding=5)
    cuaderno.add(page3, text=" Help ", padding=5)
    
    newbtn = ttk.Button(page1, text = "New")
    openbtn = ttk.Button(page1, text = "Open")
    savebtn =  ttk.Button(page1, text = "Save")
    saveasbtn = ttk.Button(page1, text = "Save As")
    closebtn = ttk.Button(page1, text = "Close")
    newbtn.pack(side = LEFT, expand = True, fill = BOTH)
    openbtn.pack(side = LEFT, expand = True, fill = BOTH)
    savebtn.pack(side = LEFT, expand = True, fill = BOTH)
    saveasbtn.pack(side = LEFT, expand = True, fill = BOTH)
    closebtn.pack(side = LEFT, expand = True, fill = BOTH)
    
    cutbtn = ttk.Button(page2, text = "Cut").pack(side = LEFT, expand = True, fill = BOTH)
    copybtn = ttk.Button(page2, text = "Copy").pack(side = LEFT, expand = True, fill = BOTH)
    pastebtn = ttk.Button(page2, text = "Paste").pack(side = LEFT, expand = True, fill = BOTH)
    undobtn = ttk.Button(page2, text = "Undo").pack(side = LEFT, expand = True, fill = BOTH)
    redobtn = ttk.Button(page2, text = "Redo").pack(side = LEFT, expand = True, fill = BOTH)  
    
    tutobtn = ttk.Button(page3, text = "Tutorial").pack(side = LEFT, expand = True, fill = BOTH)  
    aboutbtn = ttk.Button(page3, text = "About").pack(side = LEFT, expand = True, fill = BOTH)
    
    content.grid(column=0, row=0, sticky="nsew")
    lateral.grid(column=0, row=0, rowspan=3, sticky="nsew")
    notebook.grid(column=1, row=0, columnspan=2, sticky="nsew")
    cuaderno.pack(expand = "true", fill="both")
    workarea.grid(column=1, row=1, columnspan=2, rowspan=2, sticky="nsew")
    
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    content.grid_columnconfigure(0, weight=1)
    content.grid_columnconfigure(1, weight=20)
    content.grid_rowconfigure(0, weight=1)
    content.grid_rowconfigure(1, weight=5)
    notebook.grid_columnconfigure(0, weight=1)
    notebook.grid_columnconfigure(1, weight=1)
    workarea.grid_columnconfigure(0, weight=1)
    workarea.grid_rowconfigure(0, weight=1)
    show_welcome()
    
    root.mainloop()