name = input("Name:")
age = int(input("Age: "))
height = float(input("Height (m): "))
is_pm = input("Are you a pm? (yes/no): ").strip().lower() == "y"

future_age = age + 5
height_cm = int(height * 100)
print(f"{name}. In 5 years, you'll be {future_age}. Your height is {height_cm} cm. PM: {is_pm}")