data = input("Nhập chuỗi nhị phân 4 chữ số, cách nhau dấu phẩy: ")
items = data.split(",")

result = []
for item in items:
    if int(item, 2) % 5 == 0:
        result.append(item)

print(",".join(result))
