from tkinter import * #Import spects from tkinter library
from tkinter import simpledialog, colorchooser
import random, time, threading
master = Tk() #Iniialise master window
root = Frame(master, width=100, height=100)
root.pack_propagate(0) #Dont allow widgets to resize it
root.pack()
def btn_pressed(*args):
    simpledialog.messagebox.showinfo("Hello!", "I see you have clicked my button! Now Pick A Colour For It!", parent=root) #Alert box
    rgbColour, hexColour = colorchooser.askcolor(parent=root) #Color picker
    btn.config(bg=hexColour) #Change button colour
    def expand():
        for i in range(0, 100):
            root.config(height=root.winfo_height() + 1, width=root.winfo_width() + 1)
            time.sleep(0.1)
        time.sleep(1)
        label.configure(text="See you later!")
        time.sleep(1)
        label.place_forget()
    threading.Thread(target=expand).start()
btn = Button(root, text='Click Me', command=btn_pressed)
btn.pack()
label = Label(root, text="Oh, you found me")
label.place(x=50, y=130)
root.mainloop()
