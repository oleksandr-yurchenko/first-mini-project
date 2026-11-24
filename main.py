from decimal import Decimal
#1 1. запитати про суму рахунку 2. відсоток чайових(потім перевести щоб порахувати) 3. кількість людей
bill = Decimal(input("Вкажіть суму рахунку: "))
tips = int(input("Вкажіть відсоток чайових :"))
number = float(input("Вкажіть кількість людей :"))
print("")
print("")
print("")
suma = bill 
chelovek = number



#2 1.написати скыльки виходить сума разом з чайовими 2. вивести кількість людей 3. і порахувати і вивести скільки буде з кожного
total = Decimal(bill + ((bill * tips) / 100))

kazhdiy = (Decimal(total) / Decimal(chelovek))

percent = ((bill * tips) / 100)

#3 вирівняти за ф рядками та побудувати рамки
print("=" * 30)
print(f"{'РАХУНОК У КАФЕ':>22}")
print("=" * 30)
print(f"Сума рахунку{suma:>18.2f}")
print(f"Чайові {tips:>4}%{percent:>18.2f}")
print("-" * 30)
print(f"Разом{total:>25.2f}  ")
print(f"Людей{chelovek:>25.0f}    ")
print(f"З кожного{kazhdiy:>21.2f}  ")
print("=" * 30)
#4 перевірити то все на калькуляторі та потім спробувати зробити бонус  