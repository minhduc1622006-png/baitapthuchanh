print("tran minh duc")

class hinhchunhat(object):
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong

    def dientich(self):
        return self.dai * self.rong

if __name__ == "__main__":
    try:
        dai = float(input("Nhập chiều dài: "))
        rong = float(input("Nhập chiều rộng: "))
    except ValueError:
        print("Lỗi: Vui lòng nhập số hợp lệ.")
        exit()

    hcn = hinhchunhat(dai, rong)
    print("Diện tích hình chữ nhật là:", hcn.dientich())
