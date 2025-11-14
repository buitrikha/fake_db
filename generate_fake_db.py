import mysql.connector
from faker import Faker
import random
from datetime import datetime, timedelta

# Khởi tạo Faker với locale tiếng Việt
fake = Faker('vi_VN')

# Kết nối MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    port=3306,  
    password='kha11',  
    database='QLSINHVIEN'
)
cursor = conn.cursor()

print("Bắt đầu tạo dữ liệu fake...")

# 1. Tạo KHOA (10 khoa)
print("Đang tạo dữ liệu KHOA...")
khoa_list = []
khoa_names = [
    'Công nghệ thông tin', 'Kinh tế', 'Kỹ thuật', 'Ngoại ngữ', 
    'Khoa học tự nhiên', 'Y Dược', 'Luật', 'Sư phạm',
    'Điện - Điện tử', 'Xây dựng'
]

for i in range(10):
    ma_khoa = f'K{i+1:02d}'
    khoa_list.append(ma_khoa)
    cursor.execute("""
        INSERT INTO KHOA (Ma_Khoa, Ten_Khoa, Nam_TL, Phong_Khoa)
        VALUES (%s, %s, %s, %s)
    """, (ma_khoa, khoa_names[i], random.randint(1950, 2000), f'P{i+1}'))

conn.commit()

# 2. Tạo BOMON (30 bộ môn)
print("Đang tạo dữ liệu BOMON...")
bomon_list = []
bomon_names = [
    'Lập trình', 'Mạng máy tính', 'Trí tuệ nhân tạo', 'An toàn thông tin',
    'Kế toán', 'Tài chính', 'Marketing', 'Quản trị kinh doanh',
    'Cơ khí', 'Tự động hóa', 'Điện tử viễn thông', 'Kỹ thuật xây dựng',
    'Tiếng Anh', 'Tiếng Trung', 'Tiếng Nhật', 'Tiếng Hàn',
    'Toán học', 'Vật lý', 'Hóa học', 'Sinh học',
    'Y khoa', 'Dược học', 'Điều dưỡng', 'Y tế công cộng',
    'Luật dân sự', 'Luật hình sự', 'Luật kinh tế', 'Luật quốc tế',
    'Sư phạm toán', 'Sư phạm văn'
]

for i in range(30):
    ma_bm = f'BM{i+1:02d}'
    bomon_list.append(ma_bm)
    cursor.execute("""
        INSERT INTO BOMON (Ma_BM, Ten_BM, Phong_BM, Email_BM, Ma_Khoa)
        VALUES (%s, %s, %s, %s, %s)
    """, (ma_bm, bomon_names[i], f'P{i+100}', f'bomon{i+1}@ptit.edu.vn', random.choice(khoa_list)))

conn.commit()

# 3. Tạo GIANGVIEN (200 giảng viên)
print("Đang tạo dữ liệu GIANGVIEN...")
gv_list = []
hoc_vi = ['Cử nhân', 'Thạc sĩ', 'Tiến sĩ', 'Phó Giáo sư', 'Giáo sư']

for i in range(200):
    ma_gv = f'GV{i+1:04d}'
    gv_list.append(ma_gv)
    cursor.execute("""
        INSERT INTO GIANGVIEN (Ma_GV, Ten_GV, SDT_GV, Ngay_Sinh_GV, Gioi_Tinh_GV, Email_GV, Hoc_Vi, Ma_BM)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        ma_gv,
        fake.name(),
        fake.phone_number(),
        fake.date_of_birth(minimum_age=30, maximum_age=65),
        random.choice(['Nam', 'Nữ']),
        f'gv{i+1}@ptit.edu.vn',
        random.choice(hoc_vi),
        random.choice(bomon_list)
    ))

conn.commit()

# 4. Tạo MONHOC (100 môn học)
print("Đang tạo dữ liệu MONHOC...")
monhoc_list = []
mon_hoc_names = [
    'Lập trình C', 'Lập trình Java', 'Cơ sở dữ liệu', 'Cấu trúc dữ liệu',
    'Toán cao cấp', 'Vật lý đại cương', 'Hóa học đại cương', 'Sinh học',
    'Kinh tế vĩ mô', 'Kinh tế vi mô', 'Marketing căn bản', 'Quản trị học',
    'Tiếng Anh 1', 'Tiếng Anh 2', 'Tiếng Anh 3', 'Tiếng Anh 4',
    'Triết học Mác-Lênin', 'Tư tưởng HCM', 'Đường lối ĐCS VN', 'Pháp luật đại cương',
    'Lập trình Hướng đối tượng', 'Lập trình Python', 'Lập trình Web', 'Lập trình di động',
    'Công nghệ phần mềm', 'Kiểm thử phần mềm', 'Quản lý dự án phần mềm',
    'Phân tích & Thiết kế hệ thống', 'Phân tích & Thiết kế hướng đối tượng', 'Các mẫu thiết kế',
    'Lập trình .NET', 'Tương tác Người – Máy', 'Mạng máy tính', 'Hệ điều hành',
    'Kiến trúc máy tính', 'Quản trị mạng', 'Quản trị hệ thống', 'Điện toán đám mây',
    'Lập trình hệ thống', 'Điện toán song song & Phân tán', 'Hệ quản trị Cơ sở dữ liệu',
    'Trí tuệ nhân tạo', 'Học máy', 'Khai phá dữ liệu', 'Xử lý ngôn ngữ tự nhiên',
    'Thị giác máy tính', 'Big Data', 'An toàn thông tin', 'Mật mã học', 'An ninh mạng',
    'Toán rời rạc', 'Xác suất thống kê', 'Đại số tuyến tính', 'Phương pháp tính',
    'Lý thuyết đồ thị', 'Vật lý 2', 'Toán cao cấp 3', 'Logic học',
    'Lý thuyết thông tin', 'Tối ưu hóa',
    'Kỹ thuật điện', 'Điện tử cơ bản', 'Kỹ thuật số', 'Vi xử lý & Vi điều khiển',
    'Tín hiệu và Hệ thống', 'Xử lý tín hiệu số', 'Lý thuyết điều khiển tự động',
    'Thông tin vô tuyến', 'Thông tin quang', 'Lập trình nhúng',
    'Nguyên lý Kế toán', 'Tài chính doanh nghiệp', 'Quản trị nhân sự', 'Quản trị chiến lược',
    'Thương mại điện tử', 'Hệ thống thông tin quản lý', 'Luật kinh tế', 'Luật Sở hữu trí tuệ',
    'Quản trị rủi ro', 'Logistics và Quản lý chuỗi cung ứng',
    'Kinh tế chính trị Mác-Lênin', 'Chủ nghĩa xã hội khoa học', 'Lịch sử Đảng Cộng sản Việt Nam',
    'Tâm lý học đại cương', 'Xã hội học đại cương', 'Cơ sở văn hóa Việt Nam', 'Lịch sử văn minh thế giới',
    'Nhập môn Truyền thông', 'Đạo đức kỹ thuật', 'Tiếng Nhật',
    'Giáo dục thể chất 1', 'Giáo dục thể chất 2', 'Giáo dục thể chất 3',
    'Giáo dục Quốc phòng & An ninh 1', 'Giáo dục Quốc phòng & An ninh 2', 'Giáo dục Quốc phòng & An ninh 3',
    'Phương pháp nghiên cứu khoa học', 'Kỹ năng mềm', 'Tư duy phản biện', 'Khởi nghiệp & Đổi mới sáng tạo'
]

# Tạo thêm môn học để đủ 100
for i in range(100):
    ma_mh = f'MH{i+1:03d}'
    monhoc_list.append(ma_mh)
    ten_mh = mon_hoc_names[i]
    cursor.execute("""
        INSERT INTO MONHOC (Ma_MH, Ten_MH, So_Tiet_LT, So_Tiet_TH, So_Tin_Chi, Ma_BM)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        ma_mh,
        ten_mh,
        random.choice([30, 45, 60]),
        random.choice([0, 15, 30]),
        random.choice([2, 3, 4]),
        random.choice(bomon_list)
    ))

conn.commit()

# 5. Tạo LOPHANHCHINH (50 lớp)
print("Đang tạo dữ liệu LOPHANHCHINH...")
lhc_list = []
for i in range(50):
    ma_lhc = f'LHP{i+1:03d}'
    lhc_list.append(ma_lhc)
    cursor.execute("""
        INSERT INTO LOPHANHCHINH (Ma_LHP, Ma_Lop, Ten_Lop, SI_So, Nien_Khoa, Ma_Khoa)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        ma_lhc,
        f'L{i+1:02d}',
        f'Lớp {random.choice(["CNTT", "KT", "KT", "NN"])} K{random.randint(18, 23)}',
        random.randint(30, 50),
        f'{2018+i//10}-{2022+i//10}',
        random.choice(khoa_list)
    ))

conn.commit()

# 6. Tạo SINHVIEN (1000 sinh viên)
print("Đang tạo dữ liệu SINHVIEN...")
sv_list = []
for i in range(1000):
    ma_sv = f'SV{i+1:05d}'
    sv_list.append(ma_sv)
    ho_ten = fake.name().split()
    cursor.execute("""
        INSERT INTO SINHVIEN (Ma_SV, HoDemSV, Ten_SV, Ngay_Sinh_SV, SDT_SV, Email_SV, TT_Hoctap, Dia_Chi, Ma_Lop)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        ma_sv,
        ' '.join(ho_ten[:-1]),
        ho_ten[-1],
        fake.date_of_birth(minimum_age=18, maximum_age=25),
        fake.phone_number(),
        f'sv{i+1}@student.edu.vn',
        random.choice(['Đang học', 'Bảo lưu', 'Tốt nghiệp']),
        fake.address(),
        random.choice(lhc_list)
    ))

conn.commit()

# 7. Tạo HOCKY (10 học kỳ)
print("Đang tạo dữ liệu HOCKY...")
hk_list = []
for i in range(10):
    ma_hk = f'HK{i+1:02d}'
    hk_list.append(ma_hk)
    nam = 2020 + i // 2
    ky = (i % 2) + 1
    cursor.execute("""
        INSERT INTO HOCKY (Ma_HK, Ten_HK, Nam_Hoc, Ky_Trong_Nam, Ngay_Bat_Dau, Ngay_Ket_Thuc)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        ma_hk,
        f'Học kỳ {ky} năm học {nam}-{nam+1}',
        f'{nam}-{nam+1}',
        ky,
        datetime(nam, 9 if ky == 1 else 2, 1),
        datetime(nam+1 if ky == 1 else nam, 1 if ky == 1 else 6, 15)
    ))

conn.commit()

# 8. Tạo LOPHOCPHAN (300 lớp học phần)
print("Đang tạo dữ liệu LOPHOCPHAN...")
lhp_list = []
phong_hoc = ['A101', 'A102', 'B201', 'B202', 'C301', 'C302', 'D401', 'D402']
for i in range(300):
    ma_lhp = f'LHP{i+1:04d}'
    lhp_list.append(ma_lhp)
    cursor.execute("""
        INSERT INTO LOPHOCPHAN (Ma_LHP, SL_Toi_Da, Phong_Hoc, Lich_Hoc, Ma_MH, Ma_HK, Ma_GV)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (
        ma_lhp,
        random.randint(40, 60),
        random.choice(phong_hoc),
        f'Thứ {random.randint(2, 7)}, tiết {random.randint(1, 10)}-{random.randint(11, 12)}',
        random.choice(monhoc_list),
        random.choice(hk_list),
        random.choice(gv_list)
    ))

conn.commit()

# 9. Tạo DANGKY (2000 bản ghi đăng ký)
print("Đang tạo dữ liệu DANGKY...")
dangky_set = set()
while len(dangky_set) < 2000:
    sv = random.choice(sv_list)
    lhp = random.choice(lhp_list)
    dangky_set.add((sv, lhp))

for sv, lhp in dangky_set:
    cursor.execute("""
        INSERT INTO DANGKY (Ma_SV, Ma_LHP)
        VALUES (%s, %s)
    """, (sv, lhp))

conn.commit()

# 10. Tạo DIEM (1500 bản ghi điểm)
print("Đang tạo dữ liệu DIEM...")
diem_list = random.sample(list(dangky_set), 1500)
for sv, lhp in diem_list:
    cursor.execute("""
        INSERT INTO DIEM (Ma_SV, Ma_LHP, Diem_CC, Diem_GK, Diem_CK)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        sv,
        lhp,
        round(random.uniform(5, 10), 1),
        round(random.uniform(4, 10), 1),
        round(random.uniform(4, 10), 1)
    ))

conn.commit()

# Đóng kết nối
cursor.close()
conn.close()

print("✅ Hoàn thành! Đã tạo:")
print("- 10 Khoa")
print("- 30 Bộ môn")
print("- 200 Giảng viên")
print("- 100 Môn học")
print("- 50 Lớp hành chính")
print("- 1000 Sinh viên")
print("- 10 Học kỳ")
print("- 300 Lớp học phần")
print("- 2000 Đăng ký")
print("- 1500 Điểm")