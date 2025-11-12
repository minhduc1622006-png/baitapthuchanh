danh_sach_dau_vao = [1, 2, 3, 4, 5, 6, 7, 8, 9]
danh_sach_ket_qua = []
for so in danh_sach_dau_vao:
    if so % 2 != 0:
        danh_sach_ket_qua.append(so)
print(danh_sach_ket_qua)
