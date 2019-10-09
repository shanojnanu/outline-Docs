import time
from os import path
from tkinter import *
from tkinter.ttk import Progressbar
from pygame import image
import tkinter.messagebox
from tkinter import filedialog, messagebox
import webbrowser
from ttkthemes import themed_tk as tk
import global_var
from main import main




#main App
out=Tk()

#varibles and gui
open = PhotoImage(file=r'images\input_icon.png')
filename=''
k=0
source=''
summary=PhotoImage(file=r'images\make_summary.png')
cmpny_ico=PhotoImage(file=r'images\expleo-ico.png')


#title
out.title('Outline-docs')
out.iconbitmap(r'images\out-line.ico')
out.geometry('400x300')

#methods-commands(
def open_File():
    global filename
    global source
    inputfiletext.delete('1.0', END)
    filename=filedialog.askopenfilename(defaultextension=".pdf",filetypes=[('pdf file', '*.pdf')])
    source=filename
    inputfiletext.insert(tkinter.END,filename)
    print (filename)

def click_Togenerate_summmary():
    global filename
    global source
    global k
    time.sleep(1)
    progres["value"] = 0
    progres.update()
    k=0
    label1['text'] = ''
    label1.place_forget()
    if filename.strip():
        #gui_btngenerateSummary.place_forget()#hide element
        update_progress(k,10)
        #time.sleep(3)
        link1['text']=path.dirname(filename)
        #print(path.dirname(filename))
        f_path=path.dirname(filename)
        print(f_path)
        base=path.basename(filename)
        f_name=path.splitext(base)[0]
        print(f_name)
        update_progress(k,25)
        #print(path.splitext(base)[0])
        filename=main(f_path,f_name)
        update_progress(k,75)
        link1['text'] = global_var.reportfilepath
        link1.bind("<Button-1>", callback)
        update_progress(k,101)
        filename = source
        messagebox.showinfo("SUCCESS!", "Find your report at '" + global_var.reportfilepath + "'")
    else:
        messagebox.showwarning("No File!", "NO FILE WAS SELECTED")

def callback(event):
    webbrowser.open_new(event.widget.cget("text"))

def update_progress(m,n):
    global k
    for i in range(m,n):
        time.sleep(0.05)
        progres["value"] = i
        progres.update()
        if(i%5 is 0):
            processing(i)
            time.sleep(0.1)
            k=i

def processing(percent):
    label1['text']='Processing '+str(percent)+'%'
    label1.place(x=20, y=80)
    time.sleep(0.5)
    for j in [1,2,3]:
        label1['text']=label1['text']+('.'*j)
        label1.place(x=20, y=80)



#)
#gui-elements
#(

#element-1
#menu-bar
menubar = Menu(out)
out.config(menu=menubar)

#submenu - File
submenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=submenu)
submenu.add_command(label='Open',command=open_File)
submenu.add_command(label='Exit',command=out.destroy)



#element-2

#submenu - Help
submenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Help',menu=submenu)
submenu.add_command(label='About')

#element-3
frame1 = Frame(out)
frame1.pack(side=TOP)

inputfiletext = Text(frame1, height=1, width=40)
inputfiletext.pack(side='right')

#element-4
guibtnOpen = Button(frame1, image=open,command=open_File)
guibtnOpen.pack(side='left')
# #)

frame2 = Frame(out)
frame2.pack(fill=BOTH, expand=True)

#element-5
gui_btngenerateSummary=Button(frame2, image=summary, command=click_Togenerate_summmary)
gui_btngenerateSummary.place(x=150,y=0)

#element-6
progres = Progressbar(frame2, orient = 'horizontal', length = 300, mode = 'determinate', maximum=100)
progres.place(x=20,y=50)

# #frame
frame = Frame(out, bd=1, relief=SUNKEN)
frame.pack(side=BOTTOM, fill="both")

#status bar
statusbar = Label(frame,text='Make a Outline of your docs...', anchor=W)
statusbar.pack(side='left')
img_stat = Label(frame, image=cmpny_ico)
img_stat.pack(side='right')

link1 = Label(frame2, text=filename, fg="blue", cursor="hand2")
link1.place(x=20,y=100)

label1=Label(frame2,text='Processing')

def on_closing():
    out.destroy()

out.protocol("WM_DELETE_WINDOW", on_closing)
#Construct
out.mainloop()