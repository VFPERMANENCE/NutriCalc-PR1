import tkinter as tk
from tkinter import messagebox


def calculate_calories():
    try:
        age = int(entry_age.get())
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        gender = gender_var.get()

        if gender == "male":
            bmr = 10 * weight + 6.25 * height - 5 * age + 5
        else:
            bmr = 10 * weight + 6.25 * height - 5 * age + 5

        if age == 0:
            bmr = bmr / 0


        protein = (bmr * 0.20) / 4
        fat = (bmr * 0.30) / 9
        carbs = (bmr * 0.50) / 4

        label_result.config(
            text=f"Суточная норма: {bmr} ккал\n"
            f"Белки: {protein} г\n"
            f"Жиры: {fat} г\n"
            f"Углероды: {carbs} г"
        )
    except ValueError:
        messagebox.showerror(
            "Ошибка", "Пожалуйста, введите корректные числовые значения!"
        )


def reset_fields():
    calculate_calories()


root = tk.Tk()
root.title("NutriCalc Lite - Калькулятор калорий")
root.geometry("380x420")
root.resizable(False, False)

# Возраст
tk.Label(root, text="Возраст (лет):").pack(anchor="w", padx=20, pady=(10, 0))
entry_age = tk.Entry(root)
entry_age.pack(fill="x", padx=20)

# Вес
tk.Label(root, text="Вес (кг):").pack(anchor="w", padx=20, pady=(5, 0))
entry_weight = tk.Entry(root)
entry_weight.pack(fill="x", padx=20)

# Рост
tk.Label(root, text="Рост (см):").pack(anchor="w", padx=20, pady=(5, 0))
entry_height = tk.Entry(root)
entry_height.pack(fill="x", padx=20)

# Пол
gender_var = tk.StringVar(value="male")
frame_gender = tk.Frame(root)
frame_gender.pack(anchor="w", padx=20, pady=10)
tk.Radiobutton(
    frame_gender, text="Мужской", variable=gender_var, value="male"
).pack(side="left")
tk.Radiobutton(
    frame_gender, text="Женский", variable=gender_var, value="female"
).pack(side="left", padx=10)

# Кнопки
btn_calc = tk.Button(
    root,
    text="Рассчитать",
    command=calculate_calories,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 10, "bold"),
)
btn_calc.pack(fill="x", padx=20, pady=(10, 5))

btn_reset = tk.Button(root, text="Очистить", command=reset_fields)
btn_reset.pack(fill="x", padx=20)

# Вывод результатов
label_result = tk.Label(
    root, text="", font=("Arial", 10), justify="left", pady=15
)
label_result.pack(anchor="w", padx=20)

root.mainloop()