import tkinter as tk
from tkinter import messagebox


# Функція для обчислення абсолютної та відносної похибок
def calculate_errors(value, n_decimal_places, wide=False):
    if wide:
        # Абсолютна похибка у широкому розумінні
        abs_error = 10 ** (-n_decimal_places)
    else:
        # Абсолютна похибка у вузькому розумінні
        abs_error = 0.5 * 10 ** (-n_decimal_places)

    # Відносна похибка
    rel_error = abs_error / value

    return abs_error, rel_error


# Функція для виведення результатів
def show_results():
    try:
        value1 = float(entry_value1.get())
        n_dec1 = int(entry_dec1.get())
        abs_error1, rel_error1 = calculate_errors(value1, n_dec1, wide=False)

        value2 = float(entry_value2.get())
        n_dec2 = int(entry_dec2.get())
        abs_error2, rel_error2 = calculate_errors(value2, n_dec2, wide=True)

        result_message = (f"Перше число (вузьке розуміння):\n"
                          f"  Абсолютна похибка = {abs_error1}\n"
                          f"  Відносна похибка = {rel_error1:.6f}\n\n"
                          f"Друге число (широке розуміння):\n"
                          f"  Абсолютна похибка = {abs_error2}\n"
                          f"  Відносна похибка = {rel_error2:.6f}")

        messagebox.showinfo("Результати", result_message)

    except ValueError:
        messagebox.showerror("Помилка введення", "Введіть коректні числові значення!")


# Створення вікна програми
root = tk.Tk()
root.title("Обчислення похибок")

font_large = ("Arial", 14)

# Елементи інтерфейсу для першого числа (вузьке розуміння)
label_value1 = tk.Label(root, text="Перше число (вузьке розуміння):", font=font_large)
label_value1.pack()

entry_value1 = tk.Entry(root, font=font_large)
entry_value1.pack()

label_dec1 = tk.Label(root, text="Кількість десяткових знаків для першого числа:", font=font_large)
label_dec1.pack()

entry_dec1 = tk.Entry(root, font=font_large)
entry_dec1.pack()

# Елементи інтерфейсу для другого числа (широке розуміння)
label_value2 = tk.Label(root, text="Друге число (широке розуміння):", font=font_large)
label_value2.pack()

entry_value2 = tk.Entry(root, font=font_large)
entry_value2.pack()

label_dec2 = tk.Label(root, text="Кількість десяткових знаків для другого числа:", font=font_large)
label_dec2.pack()

entry_dec2 = tk.Entry(root, font=font_large)
entry_dec2.pack()

# Кнопка для обчислення похибок
calculate_button = tk.Button(root, text="Обчислити похибки", font=font_large,bg="#4caf50", fg="white",
                             command=show_results)
calculate_button.pack()

root.mainloop()
