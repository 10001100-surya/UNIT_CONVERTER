from tkinter import Tk,Label,Button,Entry,Spinbox

def converter_function():
    convert_this = float(user_input.get())
    unit_1 = spinbox_1.get()
    unit_2 = spinbox_2.get()

    if unit_1 =="kilometer" and unit_2=="mile":
        ans_1 = round(convert_this * 0.621371,3)
        my_result.config(text=f"{ans_1}")

    if unit_1 =="mile" and unit_2=="kilometer":
        ans_2 = round(convert_this * 1.60934,3)
        my_result.config(text=f"{ans_2}")

    if unit_1 =="meter" and unit_2=="kilometer":
        ans_3 = round(convert_this * 0.001,3)
        my_result.config(text=f"{ans_3}")


    if unit_1 =="kilometer" and unit_2=="meter":
        ans_4 = round(convert_this * 1000,3)
        my_result.config(text=f"{ans_4}")


    if unit_1 =="meter" and unit_2=="mile":
        ans_5 = round(convert_this * 0.0006,3)
        my_result.config(text=f"{ans_5}")

    if unit_1 =="mile" and unit_2=="meter":
        ans_6 = round(convert_this * 1609.34350,3)
        my_result.config(text=f"{ans_6}")

window = Tk()
window.title("Unit Converter")
window.config(padx=20,pady=20)



user_input = Entry()
user_input.grid(column= 1,row =0 )

spinbox_1 = Spinbox(values=("kilometer", "mile","meter"), width=10)
spinbox_1.grid(column = 2, row =0)
# miles_label = Label(text= "miles",font=("Arial", 16, "bold"))
# miles_label.grid(column=2,row=0)

equal_label = Label(text= "is equal to ",font=("Arial", 12, "bold"))
equal_label.grid(column=0,row=1)

my_result = Label(text= "",font=("Arial", 16, "bold"))
my_result.grid(column=1,row=1)


spinbox_2 = Spinbox(values=("kilometer", "mile","meter"), width=10)
spinbox_2.grid(column = 2, row =1)

# km_label = Label(text="KM",font=("Arial", 16, "bold"))
# km_label.grid(column=2,row=1)

calculat_button = Button(text="calculate",command=converter_function, font=("Arial", 8, "bold"))
calculat_button.grid(column=1,row=2)




window.mainloop()
