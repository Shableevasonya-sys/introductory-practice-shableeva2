# Вариант 1. Калькулятор рентабельности
def calculate_profitability(revenue, expenses):
    profit = revenue - expenses
    profitability = profit / revenue * 100
    return profit, profitability

# Ввод данных о компании
company_name = input("Введите название компании: ")
company_revenue = float(input("Введите выручку компании: "))
company_expenses = float(input("Введите затраты компании: "))
# Проверка выручки и расчет показателей
if company_revenue <= 0:
    print("Выручка должна быть больше нуля")
else:
    company_profit, sales_profitability = calculate_profitability(company_revenue, company_expenses)
    is_profitable = company_profit > 0
    # Оценка уровня рентабельности
    if sales_profitability > 20:
        profitability_level = "высокая"
    elif sales_profitability >= 10:
        profitability_level = "средняя"
    else:
        profitability_level = "низкая"
    # Вывод мини-отчета
    report_lines = [
        f"Компания: {company_name}",
        f"Прибыль: {company_profit} руб.",
        f"Рентабельность продаж: {round(sales_profitability, 2)}%",
        f"Оценка рентабельности: {profitability_level}",
        f"Компания прибыльна: {is_profitable}",
    ]
    for report_line in report_lines:
        print(report_line)
