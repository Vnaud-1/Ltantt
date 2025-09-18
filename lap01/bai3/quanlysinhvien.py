from sinhvien import SinhVien

class QuanLySinhVien:
    def __init__(self):
        self.ds = []

    def them(self, sv):
        self.ds.append(sv)

    def cap_nhat(self, id, ten=None, gioi_tinh=None, chuyen_nganh=None, diem_tb=None):
        for sv in self.ds:
            if sv.id == id:
                if ten: sv.ten = ten
                if gioi_tinh: sv.gioi_tinh = gioi_tinh
                if chuyen_nganh: sv.chuyen_nganh = chuyen_nganh
                if diem_tb is not None: sv.diem_tb = diem_tb
                return True
        return False

    def xoa(self, id):
        self.ds = [sv for sv in self.ds if sv.id != id]

    def tim_kiem(self, ten):
        return [sv for sv in self.ds if ten.lower() in sv.ten.lower()]

    def sap_xep_diem(self):
        self.ds.sort(key=lambda x: x.diem_tb, reverse=True)

    def sap_xep_chuyen_nganh(self):
        self.ds.sort(key=lambda x: x.chuyen_nganh)

    def hien_thi(self):
        for sv in self.ds:
            print(sv)
