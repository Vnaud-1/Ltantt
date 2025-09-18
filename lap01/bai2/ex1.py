nums = [int(x) for x in input("Nhập list số, cách nhau bằng dấu phẩy: ").split(",")]
even_sum = sum([n for n in nums if n % 2 == 0])
print("Tổng số chẵn:", even_sum)
