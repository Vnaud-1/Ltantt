hours = float(input("Nhập số giờ làm việc trong tuần: "))
rate = float(input("Nhập lương theo giờ: "))

if hours <= 44:
    salary = hours * rate
else:
    salary = 44 * rate + (hours - 44) * rate * 1.5

print(f"Lương thực nhận: {salary}")
