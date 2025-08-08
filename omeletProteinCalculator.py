import tkinter as tk
from tkinter import messagebox

def calculate_protein():
    try:
        eggs = float(eggs_entry.get())
        bread = float(bread_entry.get())

        if eggs < 0 or bread < 0:
            messagebox.showerror("Invalid input", "Don't enter negative numbers, cocksucker.")
            return

        protein_eggs = 6  # grams
        protein_bread = 2  # grams
        protein_total = (eggs * protein_eggs) + (bread * protein_bread)

        if eggs == 0 and bread > 0:
            result_label.config(text="Roughly %0.1f grams of protein.\nBut that ain't an omelet, it's toast with ambition." % protein_total)

        elif eggs == 0 and bread == 0:
            result_label.config(text="Good luck biting air.")
        else:
            result_label.config(text="The omelet has roughly %0.1f grams of protein." % protein_total)
            

    except ValueError:
        messagebox.showerror("Invalid input", "Enter valid numbers for both eggs and bread.")

# Create the main window
window = tk.Tk()
window.geometry("600x400")
window.title("Omelet Protein Calculator")
window.configure(bg='teal')


# Create widgets
label_font = ("Arial", 20)
label_font1 = ('Arial', 18)
entry_font = ('Arial', 15)

eggs_label = tk.Label(text="How many eggs does the omelet contain?:", font=label_font, background = 'teal')
eggs_entry = tk.Entry(width=50, font=entry_font, background = 'white')
bread_label = tk.Label(text="Input the number of bread loaves used in the omelet.:", font=label_font1, background = 'teal')
bread_entry = tk.Entry(width = 50, font=entry_font,background = 'white')
result_label = tk.Label(text="", font=label_font, background = 'teal')
calculate_button = tk.Button(text="Calculate Protein", command=calculate_protein, font=label_font, background = 'teal')



# Add widgets to the window with padding
eggs_label.pack(pady=(20, 5))
eggs_entry.pack(pady=(0, 10))
bread_label.pack(pady=(10, 5))
bread_entry.pack(pady=(0, 10))
calculate_button.pack(pady=(20, 10))
result_label.pack(pady=(10, 10))
result_label.config(justify="center")


# Run the main loop
window.mainloop()
