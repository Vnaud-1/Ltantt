d = {"a": 1, "b": 2, "c": 3}
print("Dictionary ban đầu:", d)
key = input("Nhập key muốn xóa: ")
if key in d:
    del d[key]
    print("Sau khi xóa:", d)
else:
    print("Key không tồn tại!")
