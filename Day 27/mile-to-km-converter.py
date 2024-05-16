from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=15, pady=15)

#Input
input_miles = Entry(width=10)
input_miles.grid(row=0, column=1)

#Label
miles = Label(text="Miles", font=("Arial", 14, "bold"))
miles.grid(row=0, column=2)
miles.config(padx=30, pady=5)

isequalto = Label(text=" is equal to", font=("Arial", 14, "bold"))
isequalto.grid(column=0, row=1)
isequalto.config(padx=20, pady=5)


answer_label = Label(text="0", font=("Arial", 14, "bold"))
answer_label.grid(row=1, column=1)
answer_label.config(padx=5, pady=3)

Km = Label(text=" Km", font=("Arial", 14, "bold"))
Km.grid(row=1, column=2)

#Button
def miles_to_km():
    answer = float(input_miles.get()) * 1.60934
    answer_label.config(text=round(answer, 2))


btn = Button(text="Calculate", command=miles_to_km)
btn.grid(row=2, column=1)
btn.config(pady=5)



window.mainloop()


