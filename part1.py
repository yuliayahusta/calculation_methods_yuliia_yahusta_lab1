import math
import tkinter as tk
from tkinter import messagebox


# Функція для обчислення відносної похибки
def calculate_relative_error(approx_value, true_value):
    """
    Обчислює відносну похибку між наближеним та точним значеннями.

    :param approx_value: наближене значення
    :param true_value: точне значення
    :return: відносна похибка
    """
    return abs(approx_value - true_value) / true_value


# Функція для обчислення і виведення результатів
def calculate():
    try:
        # Отримуємо значення з полів введення
        n1 = float(entry_n1.get())
        x1_approx = float(entry_x1.get())

        # Обчислення для sqrt(n1)
        X1 = math.sqrt(n1)
        dx1 = calculate_relative_error(x1_approx, X1)

        # Обчислення для n2 / N2
        n2 = float(entry_n2.get())
        N2 = float(entry_N2.get())
        x2_approx = float(entry_x2.get())
        X2 = n2 / N2
        dx2 = calculate_relative_error(x2_approx, X2)

        # Виведення результатів
        result_sqrt.set(f"sqrt({n1}) = {X1:.5f}, відносна похибка = {dx1:.5f}")
        result_div.set(f"{n2} / {N2} = {X2:.5f}, відносна похибка = {dx2:.5f}")

        # Порівняння точності
        if dx1 < dx2:
            messagebox.showinfo("Результат", f"sqrt({n1}) більш точний")
        else:
            messagebox.showinfo("Результат", f"{n2} / {N2} більш точний")

    except ValueError:
        messagebox.showerror("ПОМИЛКА", "ВВедіть валідні числа, будь ласка")


# Oсновне вікно
window = tk.Tk()
window.title("Relative Error Calculator")
window.configure(bg="#f0f0f0")

# Стиль для віджетів
label_font = ("Helvetica", 14)
entry_font = ("Helvetica", 14)
button_font = ("Helvetica", 14, "bold")

# Поля для введення n1, x1, n2, N2, x2
tk.Label(window, text="n1:", font=label_font, bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=5)
entry_n1 = tk.Entry(window, font=entry_font)
entry_n1.grid(row=0, column=1, padx=10, pady=5)

tk.Label(window, text="Приблизне значення sqrt(n1):", font=label_font, bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=5)
entry_x1 = tk.Entry(window, font=entry_font)
entry_x1.grid(row=1, column=1, padx=10, pady=5)

tk.Label(window, text="n2:", font=label_font, bg="#f0f0f0").grid(row=2, column=0, padx=10, pady=5)
entry_n2 = tk.Entry(window, font=entry_font)
entry_n2.grid(row=2, column=1, padx=10, pady=5)

tk.Label(window, text="N2:", font=label_font, bg="#f0f0f0").grid(row=3, column=0, padx=10, pady=5)
entry_N2 = tk.Entry(window, font=entry_font)
entry_N2.grid(row=3, column=1, padx=10, pady=5)

tk.Label(window, text="Приблизне значення n2/N2:", font=label_font, bg="#f0f0f0").grid(row=4, column=0, padx=10, pady=5)
entry_x2 = tk.Entry(window, font=entry_font)
entry_x2.grid(row=4, column=1, padx=10, pady=5)

# Кнопка для обчислення
calculate_button = tk.Button(window, text="Розрахувати", font=button_font, bg="#4caf50", fg="white", command=calculate)
calculate_button.grid(row=5, column=0, columnspan=2, pady=10, padx=10)

# Поля для виведення результатів
result_sqrt = tk.StringVar()
tk.Label(window, textvariable=result_sqrt, font=label_font, bg="#f0f0f0").grid(row=6, column=0, columnspan=2, pady=5)

result_div = tk.StringVar()
tk.Label(window, textvariable=result_div, font=label_font, bg="#f0f0f0").grid(row=7, column=0, columnspan=2, pady=5)

# Запуск програми
window.mainloop()
