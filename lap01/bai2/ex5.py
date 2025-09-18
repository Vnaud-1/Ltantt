items = input("Nhập list phần tử, cách nhau dấu phẩy: ").split(",")
count_dict = {}
for i in items:
    count_dict[i] = count_dict.get(i, 0) + 1
print("Kết quả:", count_dict)
