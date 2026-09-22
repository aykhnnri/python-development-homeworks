"""
Python Backend Development — Ev tapşırığı

Mövzular: Lists, Tuples və Dictionaries

QAYDALAR:
- Bütün tapşırıqları bir Python faylında yerinə yetir.
- Həllə aid kodu hər tapşırığın altına yaz.
- Hazır məlumatları dəyişdirmə; tələb olunan dəyişiklikləri kodla et.
- Sets, Functions, Classes və xarici kitabxanalardan istifadə etmə.
- Kodu VS Code-da işə salaraq yoxla.

Bütün tapşırıqlarda eyni onlayn mağaza nümunəsindən istifadə olunur.
"""


# ============================================================
# TAPŞIRIQ 1 — Lists: məhsulların idarə olunması
# ============================================================

# 1. Bütün məhsulları 1-dən başlayaraq nömrələyib ekranda göstər.
# 2. List-in sonuna "Monitor" əlavə et.
# 3. "Mouse" məhsulunu List-dən sil.
# 4. "Klaviatura" məhsulunun adını "Mexaniki Klaviatura" ilə əvəz et.
# 5. Məhsulların yekun sayını göstər.
#
# İpucu:
# enumerate(..., start=1), append(), remove(), index(), len()
#
# Gözlənilən yekun List:
# ['Laptop', 'Qulaqliq', 'Mexaniki Klaviatura', 'Monitor']


mehsullar = ["Laptop", "Qulaqliq", "Mouse", "Klaviatura"]


# Kodunu buraya yaz:





# ============================================================
# TAPŞIRIQ 2 — Lists: Sorting və Copying
# ============================================================

# 1. Original List-i dəyişmədən qiymətləri ucuzdan bahaya sırala.
# 2. Original List-i dəyişmədən qiymətləri bahadan ucuza sırala.
# 3. qiymetler List-inin copy()-si üzərində işləyərək
#    sonuna 350 əlavə et.
# 4. Original və kopyalanmış List-i çap et.
#    Originalda 350 olmamalıdır.
#
# İpucu:
# sorted(), sorted(..., reverse=True), copy(), append()
#
# Diqqət:
# Qiymətləri ayrıca sıralayanda onları məhsul adları ilə
# Index əsasında uyğunlaşdırma. Uyğunluq pozula bilər.


qiymetler = [1500, 120, 45, 80]


# Kodunu buraya yaz:





# ============================================================
# TAPŞIRIQ 3 — Tuples: statuslar və Unpacking
# ============================================================

# 1. icazeli_statuslar Tuple-ının birinci və sonuncu
#    elementini göstər.
#
# 2. İstifadəçidən sifariş statusunu input() ilə al.
#
# 3. Daxil edilən statusu strip().lower() ilə normallaşdır.
#
# 4. Status Tuple-da varsa "Status qebul edildi",
#    yoxdursa "Yanlis status" yaz.
#
# 5. mehsul Tuple-ını ad, qiymet və stok Variables-ına
#    Unpacking et, sonra hər üç məlumatı ekranda göstər.
#
# İpucu:
# [0], [-1], in, if/else, Tuple Unpacking


icazeli_statuslar = (
    "pending",
    "processing",
    "completed",
    "cancelled"
)

mehsul = ("Laptop", 1500, 3)


# Kodunu buraya yaz:





# ============================================================
# TAPŞIRIQ 4 — Dictionaries: qiymət kataloqu
# ============================================================

# 1. "Mouse" məhsulunun qiymətini Key vasitəsilə göstər.
#
# 2. "Monitor" məhsulunu 350 AZN qiymətlə əlavə et.
#
# 3. "Laptop" məhsulunun qiymətini 1400 AZN et.
#
# 4. İstifadəçidən məhsul adı al.
#    Varsa qiymətini, yoxdursa "Mehsul tapilmadi" yaz.
#    Olmayan Key üçün xəta yaratma.
#
# 5. Bütün məhsulları "Ad: qiymət AZN" formatında göstər.
#
# İpucu:
# dict[key], yeni Key-ə mənimsətmə, in / get(), items()


qiymet_kataloqu = {
    "Laptop": 1500,
    "Qulaqliq": 120,
    "Mouse": 45,
    "Klaviatura": 80
}


# Kodunu buraya yaz:





# ============================================================
# TAPŞIRIQ 5 — Dictionaries: stok və hesablamalar
# ============================================================

# 1. Məhsulun ümumi stok dəyərini hesabla:
#    qiymet * stok
#
# 2. Məhsuldan 2 ədəd satıldığını fərz et.
#    Satış üçün stok kifayətdirsə, stokdan 2 çıx
#    və satılan 2 ədədin ümumi məbləğini göstər.
#
# 3. Stok kifayət etmirsə,
#    "Kifayet qeder stok yoxdur" yaz.
#
# 4. Sonda qalan stoku göstər.
#
# İpucu:
# Dictionary-nin Value-larını Key vasitəsilə oxu
# və yenilə; if/else.
#
# Gözlənilən nəticə:
# Satış məbləği: 3000 AZN
# Qalan stok: 1


satis_mehsulu = {
    "id": 1,
    "ad": "Laptop",
    "qiymet": 1500,
    "stok": 3
}


# Kodunu buraya yaz:
