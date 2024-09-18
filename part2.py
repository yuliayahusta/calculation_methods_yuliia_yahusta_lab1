import tkinter as tk
from tkinter import messagebox

# Функція для обчислення похибок у вузькому розумінні
def narrow_error_calculation(value, delta_x):
    # Округлене значення
    rounded_value = round(value, 2)

    # Округлена абсолютна похибка
    delta_x_rounded = abs(rounded_value - value)

    # Загальна похибка
    delta_x_star = delta_x + delta_x_rounded

    # Динамічне визначення порогу
    threshold = max(0.005, delta_x)

    if delta_x_star < threshold:
        return rounded_value, delta_x_star
    else:
        return value, delta_x_star


# Функція для обчислення похибок у широкому розумінні
def wide_error_calculation(value, relative_error_percent):
    # Абсолютна похибка
    delta_x = value * (relative_error_percent / 100)

    # Округлене значення
    rounded_value = round(value, 2)

    # Округлена абсолютна похибка
    delta_x_rounded = abs(rounded_value - value)

    # Загальна похибка
    delta_x_star = delta_x + delta_x_rounded

    # Динамічне визначення порогу
    threshold = max(0.1, delta_x)

    if delta_x_star < threshold:
        return rounded_value, delta_x_star
    else:
        return value, delta_x_star


# Функція для вузького розуміння
def calculate_narrow():
    try:
        value = float(entry_value_narrow.get())
        delta_x = float(entry_delta_x_narrow.get())

        rounded_value, delta_x_star = narrow_error_calculation(value, delta_x)
        messagebox.showinfo("Результати Вузьке",
                            f"Округлене значення: {rounded_value}\nЗагальна похибка: {delta_x_star:.5f}")
    except ValueError:
        messagebox.showerror("Помилка", "Будь ласка, введіть коректні числа")


# Функція для широкого розуміння
def calculate_wide():
    try:
        value = float(entry_value_wide.get())
        relative_error_percent = float(entry_relative_error_wide.get())

        rounded_value, delta_x_star = wide_error_calculation(value, relative_error_percent)
        messagebox.showinfo("Результати Широке",
                            f"Округлене значення: {rounded_value}\nЗагальна похибка: {delta_x_star:.5f}")
    except ValueError:
        messagebox.showerror("Помилка", "Будь ласка, введіть коректні числа")


# Створення головного вікна
root = tk.Tk()
root.title("Обчислення похибок")

large_font = ("Helvetica", 14)

# Вузьке розуміння
label_narrow = tk.Label(root, text="Вузьке розуміння:", font=large_font)
label_narrow.grid(row=0, column=0, padx=10, pady=10)

label_value_narrow = tk.Label(root, text="Число:", font=large_font)
label_value_narrow.grid(row=1, column=0, padx=10, pady=5)
entry_value_narrow = tk.Entry(root, font=large_font)
entry_value_narrow.grid(row=1, column=1, padx=10, pady=5)

label_delta_x_narrow = tk.Label(root, text="Похибка (delta x):", font=large_font)
label_delta_x_narrow.grid(row=2, column=0, padx=10, pady=5)
entry_delta_x_narrow = tk.Entry(root, font=large_font)
entry_delta_x_narrow.grid(row=2, column=1, padx=10, pady=5)

button_narrow = tk.Button(root, text="Обчислити (Вузьке)", command=calculate_narrow, font=large_font)
button_narrow.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Широке розуміння
label_wide = tk.Label(root, text="Широке розуміння:", font=large_font)
label_wide.grid(row=4, column=0, padx=10, pady=10)

label_value_wide = tk.Label(root, text="Число:", font=large_font)
label_value_wide.grid(row=5, column=0, padx=10, pady=5)
entry_value_wide = tk.Entry(root, font=large_font)
entry_value_wide.grid(row=5, column=1, padx=10, pady=5)

label_relative_error_wide = tk.Label(root, text="Відносна похибка (%):", font=large_font)
label_relative_error_wide.grid(row=6, column=0, padx=10, pady=5)
entry_relative_error_wide = tk.Entry(root, font=large_font)
entry_relative_error_wide.grid(row=6, column=1, padx=10, pady=5)

button_wide = tk.Button(root, text="Обчислити (Широке)", command=calculate_wide, font=large_font)
button_wide.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
