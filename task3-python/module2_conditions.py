# Упражнение 1. Результат периода
monthly_profit = float(input("Введите прибыль за месяц: "))

if monthly_profit > 0:
    print("Прибыль")
elif monthly_profit < 0:
    print("Убыток")
else:
    print("Безубыточность")

# Упражнение 2. Категория бизнеса
business_revenue = float(input("Введите выручку компании: "))

if business_revenue <= 1_000_000:
    print("Микробизнес")
elif business_revenue <= 10_000_000:
    print("Малый")
elif business_revenue <= 100_000_000:
    print("Средний")
else:
    print("Крупный")

# Упражнение 3. Расчет НДФЛ
employee_salary = float(input("Введите зарплату сотрудника: "))

if employee_salary <= 50_000:
    tax_rate = 13
else:
    tax_rate = 15

income_tax = employee_salary * tax_rate / 100
salary_after_tax = employee_salary - income_tax
print(f"НДФЛ: {income_tax} руб.")
print(f"Сумма на руки: {salary_after_tax} руб.")

# Упражнение 4. Таблица умножения ставки
percent_rate = float(input("Введите процентную ставку: "))

for month_number in range(1, 13):
    multiplied_rate = percent_rate * month_number
    print(f"{percent_rate}% x {month_number} = {multiplied_rate}%")

# Упражнение 5. Анализ цен
product_prices = [120, 350, 280, 499, 75]

for product_price in product_prices:
    if product_price > 300:
        print(f"{product_price} руб. - ДОРОГО")
    else:
        print(f"{product_price} руб.")
