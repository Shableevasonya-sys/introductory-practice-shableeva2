# Упражнение 1. Функция расчета прибыли
def calculate_profit(revenue, expenses):
    return revenue - expenses


profit_examples = [
    (120000, 85000),
    (300000, 250000),
    (90000, 110000),
]

for revenue_value, expenses_value in profit_examples:
    profit_value = calculate_profit(revenue_value, expenses_value)
    print(f"Выручка: {revenue_value}, затраты: {expenses_value}, прибыль: {profit_value}")

# Упражнение 2. Функция расчета НДС
def calculate_vat(price, vat_rate=20):
    return price * vat_rate / 100


standard_vat = calculate_vat(15000)
reduced_vat = calculate_vat(15000, 10)
print(f"НДС по стандартной ставке: {standard_vat}")
print(f"НДС по сниженной ставке: {reduced_vat}")

# Упражнение 3. Функция определения категории бизнеса
def get_category(revenue):
    if revenue <= 1_000_000:
        return "микро"
    if revenue <= 10_000_000:
        return "малый"
    if revenue <= 100_000_000:
        return "средний"
    return "крупный"


revenue_examples = [800000, 5000000, 50000000, 150000000]

for revenue_value in revenue_examples:
    business_category = get_category(revenue_value)
    print(f"Выручка {revenue_value}: {business_category} бизнес")

# Упражнение 4. Функция сложного процента
def compound_interest(capital, rate, years):
    return capital * (1 + rate / 100) ** years


for term_years in [3, 5, 10]:
    final_amount = compound_interest(100000, 8, term_years)
    print(f"Сумма через {term_years} лет: {round(final_amount, 2)} руб.")

# Упражнение 5. Функция применения скидки
def apply_discount(price, discount_percent):
    return price - price * discount_percent / 100


product_prices = [1200, 3500, 990, 7800, 560]

for product_price in product_prices:
    discounted_price = apply_discount(product_price, 15)
    print(f"Цена со скидкой: {round(discounted_price, 2)} руб.")
