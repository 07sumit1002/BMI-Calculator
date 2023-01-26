import tkinter as tk
root = tk.Tk()
#set the dimensions of interface
root.geometry("130x150")
root.title("BMI Calculator")
weight_label = tk.Label(root, text="Weight (kg)")
weight_entry = tk.Entry(root)
height_label = tk.Label(root, text="Height (cm)")
height_entry = tk.Entry(root)
def calculate_bmi():
    # Get weight and height from entries
    weight = float(weight_entry.get())
    height = float(height_entry.get())
    # Calculate BMI
    bmi = weight / (height / 100) ** 2
    # Display result 
    if 0<bmi<=18.5:
        result_text.set(f"Your BMI is {bmi:.1f}\n Underweight")
        print()
    elif 25>bmi >18.5:
        result_text.set(f"Your BMI is {bmi:.1f}\n Normal weight")
    elif 25<=bmi<=29.9:
        result_text.set(f"Your BMI is {bmi:.1f}\n Overweight")
    elif bmi >=30:
        result_text.set(f"Your BMI is {bmi:.1f}\n Obese")
    else:
        result_text.set("Invalid")
calculate_button = tk.Button(root, text="Calculate", command=calculate_bmi)
result_text = tk.StringVar()
calculate_button.bind("<Enter>",lambda event: calculate_button.config(fg='blue'))
calculate_button.bind("<Leave>",lambda event: calculate_button.config(fg='black'))
result_label = tk.Label(root, textvariable=result_text)
result_label.bind("<Enter>",lambda event: result_label.config(fg='blue'))
result_label.bind("<Leave>",lambda event: result_label.config(fg='black'))
weight_label.pack()
weight_entry.pack()
height_label.pack()
height_entry.pack()
calculate_button.pack()
result_label.pack()
root.mainloop()