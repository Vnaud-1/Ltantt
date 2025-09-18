
from sinhvien import SinhVien
from quanlysinhvien import QuanLySinhVien

ql = QuanLySinhVien()

while True:
    print("\n--- Menu ---")
    print("1. Thêm sinh viên")
    print("2. Cập nhật thông tin")
    print("3. Xóa sinh viên")
    print("4. Tìm kiếm theo tên")
    print("5. Sắp xếp theo điểm TB")
    print("6. Sắp xếp theo chuyên ngành")
    print("7. Hiển thị danh sách")
    print("0. Thoát")

    choice = input("Chọn: ")

    if choice == "1":
        ten = input("Tên: ")
        gioi_tinh = input("Giới tính: ")
        chuyen_nganh = input("Chuyên ngành: ")
        diem_tb = float(input("Điểm TB: "))
        ql.them(SinhVien(ten, gioi_tinh, chuyen_nganh, diem_tb))

    elif choice == "2":
        id = int(input("ID cần cập nhật: "))
        ten = input("Tên mới (bỏ trống nếu không đổi): ") or None
        gioi_tinh = input("Giới tính mới: ") or None
        chuyen_nganh = input("Chuyên ngành mới: ") or None
        diem_tb = input("Điểm TB mới: ")
        diem_tb = float(diem_tb) if diem_tb else None
        ql.cap_nhat(id, ten, gioi_tinh, chuyen_nganh, diem_tb)

    elif choice == "3":
        id = int(input("ID cần xóa: "))
        ql.xoa(id)

    elif choice == "4":
        ten = input("Tên tìm kiếm: ")
        kq = ql.tim_kiem(ten)
        for sv in kq:
            print(sv)

    elif choice == "5":
        ql.sap_xep_diem()

    elif choice == "6":
        ql.sap_xep_chuyen_nganh()

    elif choice == "7":
        ql.hien_thi()

    elif choice == "0":
        break

    else:
        print("Lựa chọn không hợp lệ!")
