import json
import os

FILE_NAME = "UDCNTT.json"


def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    return {}


def save_data():
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(students, file, ensure_ascii=False, indent=4)

# Khởi tạo danh sách sinh viên từ file
students = load_data()

def them_lop():
    ten_lop = input("Nhập tên lớp: ").strip().lower()
    if ten_lop not in students:
        students[ten_lop] = []
        print(f"Đã tạo lớp {ten_lop}.")
        save_data()
    else:
        print("Lớp đã tồn tại!")

def xoa_lop():
    ten_lop = input("Nhập tên lớp cần xóa: ").strip().lower()
    if ten_lop in students:
        del students[ten_lop]
        save_data()
        print(f"Đã xóa lớp {ten_lop}.")
    else:
        print("Lớp không tồn tại!")

def them_sinh_vien():
    ten_lop = input("Nhập tên lớp: ").strip().lower()
    if ten_lop not in students:
        print("Lớp chưa tồn tại!")
        return
    ma_sv = input("Nhập mã số sinh viên: ").strip().lower()
    ten_sv = input("Nhập tên sinh viên: ").strip()
    for sv in students[ten_lop]:
        if sv["ma_sv"] == ma_sv:
            print("Mã số sinh viên đã tồn tại trong lớp.")
            return
    students[ten_lop].append({"ma_sv": ma_sv, "ten_sv": ten_sv})
    save_data()
    print(f"Đã thêm sinh viên {ten_sv} (MSSV: {ma_sv}) vào lớp {ten_lop}.")

def xoa_sinh_vien():
    ten_lop = input("Nhập tên lớp: ").strip().lower()
    if ten_lop not in students:
        print("Lớp không tồn tại!")
        return
    ma_sv = input("Nhập mã số sinh viên cần xóa: ").strip().lower()
    for sv in students[ten_lop]:
        if sv["ma_sv"] == ma_sv:
            students[ten_lop].remove(sv)
            save_data()
            print(f"Đã xóa sinh viên MSSV {ma_sv} khỏi lớp {ten_lop}.")
            return
    print("Sinh viên không tồn tại trong lớp.")

def tim_kiem_sinh_vien():
    ma_sv = input("Nhập mã số sinh viên cần tìm: ").strip().lower()
    for lop, ds_sv in students.items():
        for sv in ds_sv:
            if sv["ma_sv"] == ma_sv:
                print(f"Sinh viên {sv['ten_sv']} (MSSV: {ma_sv}) thuộc lớp {lop}.")
                return
    print("Không tìm thấy sinh viên.")

def chuyen_lop():
    ma_sv = input("Nhập mã số sinh viên cần chuyển lớp: ").strip().lower()
    lop_cu = input("Nhập lớp hiện tại: ").strip().lower()
    lop_moi = input("Nhập lớp mới: ").strip().lower()

    if lop_cu not in students or lop_moi not in students:
        print("Lớp không tồn tại!")
        return

    for sv in students[lop_cu]:
        if sv["ma_sv"] == ma_sv:
            students[lop_cu].remove(sv)
            students[lop_moi].append(sv)
            save_data()
            print(f"Đã chuyển sinh viên {sv['ten_sv']} (MSSV: {ma_sv}) từ {lop_cu} sang {lop_moi}.")
            return
    print("Sinh viên không tồn tại trong lớp hiện tại.")

def thong_ke():
    for lop, ds_sv in students.items():
        print(f"Lớp {lop}: {len(ds_sv)} sinh viên.")

# Giao diện menu
while True:
    print("\n--- QUẢN LÝ SINH VIÊN ---")
    print("1. Tạo lớp mới")
    print("2. Xóa lớp học")
    print("3. Thêm sinh viên vào lớp")
    print("4. Xóa sinh viên khỏi lớp")
    print("5. Tìm kiếm sinh viên")
    print("6. Chuyển lớp học cho sinh viên")
    print("7. Thống kê số lượng sinh viên của từng lớp")
    print("8. Kết thúc chương trình.")
    choice = input("Chọn chức năng: ").strip()

    if choice == "1":
        them_lop()
    elif choice == "2":
        xoa_lop()
    elif choice == "3":
        them_sinh_vien()
    elif choice == "4":
        xoa_sinh_vien()
    elif choice == "5":
        tim_kiem_sinh_vien()
    elif choice == "6":
        chuyen_lop()
    elif choice == "7":
        thong_ke()
    elif choice == "8":
        print("Kết thúc chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại.")


