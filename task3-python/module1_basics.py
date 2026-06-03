# Упражнение 1. Карточка сотрудника
employee_name = "София Шаблеева"
employee_age = 18
employee_salary = 45000.50
is_employee_working = True

print("Имя сотрудника:", employee_name)
print("Возраст:", employee_age)
print("Зарплата:", employee_salary)
print("Работает сейчас:", is_employee_working)

# Упражнение 2. Приветствие сотрудника
worker_name = input("Введите имя сотрудника: ")
office_city = input("Введите город офиса: ")
print(f"Сотрудник {worker_name} работает в офисе {office_city}")

# Упражнение 3. Стоимость заказа
product_price = float(input("Введите цену товара: "))
product_quantity = int(input("Введите количество товара: "))
order_total = product_price * product_quantity
print(f"Итоговая стоимость заказа: {order_total} руб.")

# Упражнение 4. Доход по вкладу
deposit_amount = float(input("Введите сумму вклада: "))
interest_rate = float(input("Введите ставку по вкладу (%): "))
annual_income = deposit_amount * interest_rate / 100
print(f"Доход за год составит: {annual_income} руб.")

# Упражнение 5. Конвертер валюты
dollar_rate = float(input("Введите курс доллара: "))
rubles_amount = float(input("Введите сумму в рублях: "))
dollars_amount = round(rubles_amount / dollar_rate, 2)
print(f"Сумма в долларах: {dollars_amount}")
