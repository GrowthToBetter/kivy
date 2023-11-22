import tkinter as tk
from tkinter import ttk
window= tk.Tk()
window.configure(bg="blue")
window.geometry('400x300')
window.resizable(False,False)
window.title("belajar tkinter")

#frame input
input_frame= ttk.Frame(window)
#penempatan grid,pack,place
input_frame.pack(padx=10,pady=10,fill='x',expand=True)
#komponen 
#1.nama depan
nama_depan_label=ttk.Label(input_frame,text='nama depan')
nama_depan_label.pack(padx=10,fill='x',expand=True)


#2.entry nama depan 
NAMA_DEPAN=tk.StringVar()
nama_depan_entry=ttk.Entry(input_frame,textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=10,fill='x',expand=True)


#3.nama belakang
nama_belakang_label=ttk.Label(input_frame,text='nama belakang')
nama_belakang_label.pack(padx=10,fill='x',expand=True)


#4.entry nama belakang 
NAMA_BELAKANG=tk.StringVar()
nama_belakang_entry=ttk.Entry(input_frame,textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(padx=10,fill='x',expand=True)

window.mainloop()