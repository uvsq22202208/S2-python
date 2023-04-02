import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 600

root = tk.Tk()

canvas = tk.Canvas(root, bg = "black", width = CANVAS_WIDTH, height = CANVAS_HEIGHT)

# Début de votre code
x0 = 100
x1 = CANVAS_WIDTH - 100
x2 = CANVAS_WIDTH / 2
y = CANVAS_HEIGHT / 2
y1 = 100
y2 = CANVAS_HEIGHT - 100
canvas.create_line(x2, y1, x2, y2)
canvas.create_oval(x2-50, y2-50, x2+50, y2+50, fill = "blue")
canvas.create_oval(x2 - 50, y1 - 50, x2 + 50, y1 + 50)
canvas.create_oval((x0 + x1) / 2 - 50, y + 50, (x0 + x1) / 2 + 50, y - 50)
# Fin de votre code

canvas.grid ()
root.mainloop()
