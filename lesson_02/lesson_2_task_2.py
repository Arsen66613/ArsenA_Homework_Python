def is_year_leap(year):
    if (year % 4 == 0):
        return True
    else:
        return False


year1 = 2024
year2 = 2025

x1 = is_year_leap(year1)
x2 = is_year_leap(year2)

print(f'год {year1}: {x1}')
print(f'год {year2}: {x2}')
