import tkinter as tk
import random

win = tk.Tk()
canvas = tk.Canvas(win, width=800, height=150, bg = "white")
canvas.pack()
idex = []
x = 10
y = 10
a = ["A","B","C","D","E","F","G","H","I","J"]
pocet = {}
for i in range(10):
    tag = f"tanier{i}"
    canvas.create_oval(x, y, x+60, y+60, fill="blue", outline="black", width=3, tags=tag)
    canvas.create_oval(x+10, y+10, x+50, y+50, tags=tag)
    canvas.create_text(x+30, y+30, text=a[i], fill="white", font=("Arial", 20), tags=tag)
    idex.append(tag)
    pocet[tag] = 0
    x += 80

vyherny = random.choice(idex)
print(vyherny)
def klik(event):
    global pocet
    obj = canvas.find_withtag("current")
    if obj:
        o = canvas.gettags(obj[0])[0]
        pocet[o] += 1
        if o == vyherny:
            canvas.delete("all")
            canvas.create_text(400,70,text="vyhral si",fill="red",font=("Arial", 40))
            print(pocet)


canvas.bind("<Button-1>", klik)
win.mainloop()

