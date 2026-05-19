import tkinter as tk
import random
window = tk.Tk()
canvas = tk.Canvas(window,width=800,height=200, bg="white")
canvas.pack()
taniere = []
pismena = ["A","B","C","D","E","F","G","H","I","J"]
pocet = {}
x = 10
for i in range(10):
    tag = pismena[i]
    canvas.create_oval(x,20,x+70,90, fill="red",tags=tag)
    canvas.create_oval(x+10,30,x+60,80,tags=tag)
    canvas.create_text(x+35,55,text = pismena[i],fill="white",font=("Arial",20),tags=tag)
    taniere.append(tag)
    pocet[tag] = 0
    x += 80

vyhra = random.choice(taniere)
print(vyhra)
print(taniere)
def klik(event):
    global pocet
    obj = canvas.find_withtag("current")
    if obj:
        item_id = obj[0]
        tagy = canvas.gettags(item_id)
        if tagy[0] != vyhra:
            pocet[tagy[0]] += 1
        if tagy[0] == vyhra:
            viac = []
            for a, b in pocet.items():
                if b != 0:
                    viac.append(a)
            canvas.delete("all")
            canvas.create_text(400, 70, text="vyhral si", fill="blue", font=("Arial", 40))
            canvas.create_text(400, 120, text=f"viackrát si klikol na taniere: {", ".join(viac)}", fill="red", font=("Arial", 20))
            print(viac)

canvas.bind("<Button-1>",klik)
window.mainloop()
