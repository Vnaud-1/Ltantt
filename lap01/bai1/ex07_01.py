lines = []
print("Nhập các dòng (bấm Enter trống để kết thúc):")
while True:
    line = input()
    if not line:
        break
    lines.append(line.upper())

print("\n".join(lines))
