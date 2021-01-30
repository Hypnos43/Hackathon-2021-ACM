import os
from tkinter import*
root=Tk()
root.geometry('900x200')
root.title("Graphing Calculator")
l=Label(root, text="Choose one of the given options!", font=("Arial Bold", 25))
l.grid(row=0,column=0)
def main():
    os.system('main.py')
def fourier():
    os.system('fourier.py')
def ODE_plot():
    os.system('ODEbutton.py')
def mat():
    os.system('matrix_transformation.py')
def ft():
    os.system('fourier_transformation.py')    

b1=Button(root,text="Predefined Functions",bg="yellow", fg="blue",font=("Arial Bold", 15),command=main)
b1.grid(row=2,column=0)
b2=Button(root,text="Fourier Series",bg="cyan", fg="blue",font=("Arial Bold", 15),command=fourier)
b2.grid(row=2,column=1)
b3=Button(root,text="Ordinary Differential Equation",bg="red",fg="blue",font=("Arial Bold",15),command=ODE_plot)
b3.grid(row=4,column=1)
b4=Button(root,text="Matrix Space transformation",bg="green",fg="blue",font=("Arial Bold",15),command=mat)
b4.grid(row=6,column=0)
b5=Button(root,text="A fourier Transform",bg="grey", fg="black",font=("Arial Bold", 15),command=ft)
b5.grid(row=4,column=0)
