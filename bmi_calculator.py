import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        
        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive numbers.")
        
        bmi = weight / ((height/100) ** 2)
        category = bmi_category(bmi)
        
        result_label.config(text=f"Your BMI is: {bmi}\nCategory: {category}")
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Create the main application window
root = tk.Tk()
root.title("BMI Calculator")

# Create and place the weight label and entry
label_weight = tk.Label(root, text="Enter your weight in kilograms:")
label_weight.pack()

entry_weight = tk.Entry(root)
entry_weight.pack()

# Create and place the height label and entry
label_height = tk.Label(root, text="Enter your height in centimeters:")
label_height.pack()

entry_height = tk.Entry(root)
entry_height.pack()

# Create and place the calculate button
calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack()

# Create and place the result label
result_label = tk.Label(root, text="")
result_label.pack()

# Run the application
root.mainloop()
