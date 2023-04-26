from tkinter import *

import random

root = Tk()

root.title("List Data Type Basket")

root.geometry("400x400")

item_list = ["Banana","Old Shoe","Laptop","Phone","Fork","Pepper","Water Bottle","Flower"]

list_label = Label(root, text = item_list)

list_label.place(relx = 0.5, rely = 0.3, anchor = CENTER)

basket = Label(root)

basket.place(relx = 0.5, rely = 0.5, anchor = CENTER)

def rs():
    rn = random.randint(0,7)
    ri = item_list[rn]
    print(ri)
    basket["text"] = "Put "+ri+" in your basket "
    
btn = Button(root, text = "What to put in Your Basket", command = rs)
btn.place(relx = 0.5, rely = 0.4, anchor = CENTER)

root.mainloop()