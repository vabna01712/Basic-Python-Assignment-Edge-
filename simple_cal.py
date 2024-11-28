import tkinter as tk

def handle_button_click(event):
    current_input = display.get()
    clicked_text = event.widget.cget("text")
    if clicked_text == '=':
        try:
            result = str(eval(current_input))
            display.delete(0, tk.END)
            display.insert(tk.END, result)
        except Exception:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    elif clicked_text == 'AC':
        display.delete(0, tk.END)
    else:
        display.insert(tk.END, clicked_text)

#calc window
app = tk.Tk()
app.title("Simple Calculator")

#displaying the input/output
display = tk.Entry(app, width=20, font=('Helvetica', 22), bd=5, justify='right')
display.grid(row=0, column=0, columnspan=4)

#Calculator buttons
button_labels = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'AC', '=', '+'
]

start_row = 1
start_column = 0

for label in button_labels:
    btn = tk.Button(app, text=label, font=('Helvetica', 18), width=5, height=2)
    btn.grid(row=start_row, column=start_column)
    btn.bind("<Button-1>", handle_button_click)
    start_column += 1
    if start_column > 3:
        start_column = 0
        start_row += 1

#run calc
app.mainloop()
