# ============================================================
# DƏRS 9 — HOMEWORK
# Mövzular: Sets və Functions
# ============================================================


# ------------------------------------------------------------
# TAPŞIRIQ 1 — Unique məhsul kateqoriyaları
# ------------------------------------------------------------
#
# Aşağıdakı list-də online mağazadakı məhsulların
# kateqoriyaları verilib.
#
# 1. Təkrarlanan kateqoriyaları sil.
# 2. Unique kateqoriyaları ekrana çıxar.
# 3. Neçə fərqli kateqoriya olduğunu ekrana çıxar.
#
# TIP:
# set() və len() istifadə edə bilərsən.


kateqoriyalar = [
    "Telefon",
    "Laptop",
    "Telefon",
    "Aksesuar",
    "Laptop",
    "Monitor",
    "Aksesuar",
    "Klaviatura"
]


# Kodunu burada yaz:




# ------------------------------------------------------------
# TAPŞIRIQ 2 — İki platformada olan istifadəçilər
# ------------------------------------------------------------
#
# Aşağıda iki fərqli platformada qeydiyyatdan keçmiş
# istifadəçilərin adları verilib.
#
# Həm mobil tətbiqdə, həm də web saytında qeydiyyatdan
# keçmiş istifadəçiləri tap və ekrana çıxar.
#
# Daha sonra hər iki platformadakı bütün unique istifadəçiləri
# birləşdirib ayrıca ekrana çıxar.
#
# TIP:
# intersection və union əməliyyatlarını xatırla.


mobil_istifadeciler = {
    "Kamran",
    "Leyla",
    "Orxan",
    "Aysel",
    "Rauf"
}

web_istifadeciler = {
    "Leyla",
    "Rauf",
    "Samir",
    "Aysel",
    "Nermin"
}


# Kodunu burada yaz:




# ------------------------------------------------------------
# TAPŞIRIQ 3 — Endirimli qiymət
# ------------------------------------------------------------
#
# "endirim_hesabla" adlı function yarat.
#
# Function iki parameter qəbul etməlidir:
#
# qiymet
# endirim_faizi
#
# Function endirim tətbiq olunduqdan sonra yeni qiyməti
# hesablamalı və ekrana çıxarmalıdır.
#
# Məsələn:
#
# endirim_hesabla(100, 20)
#
# Nəticə:
#
# Yeni qiymət: 80.0
#
#
# Function-u ən azı 3 fərqli qiymətlə yoxla.
#
# TIP:
#
# Endirim məbləğini belə hesablaya bilərsən:
#
# qiymet * endirim_faizi / 100


# Kodunu burada yaz:




# ------------------------------------------------------------
# TAPŞIRIQ 4 — Ədədin vəziyyətini yoxla
# ------------------------------------------------------------
#
# "ededi_yoxla" adlı function yarat.
#
# Function bir ədəd qəbul etməlidir.
#
# Əgər ədəd:
#
# 0-dan böyükdürsə:
# "Müsbət ədəd"
#
# 0-dan kiçikdirsə:
# "Mənfi ədəd"
#
# 0-a bərabərdirsə:
# "Sıfır"
#
# ekrana çıxarsın.
#
# Function-u aşağıdakı dəyərlərlə yoxla:
#
# 15
# -8
# 0
#
# TIP:
# if / elif / else istifadə et.


# Kodunu burada yaz:




# ------------------------------------------------------------
# TAPŞIRIQ 5 — Sifarişin ümumi qiyməti
# ------------------------------------------------------------
#
# "umumi_qiymeti_hesabla" adlı function yarat.
#
# Function 3 məhsulun qiymətini parameter olaraq qəbul etsin.
#
# Məhsulların ümumi qiymətini hesablasın və nəticəni
# return etsin.
#
# Function daxilində nəticəni print etmə.
#
# Function-u çağırdıqdan sonra nəticəni bir variable-da saxla
# və həmin variable-ı print et.
#
# Məsələn:
#
# umumi = umumi_qiymeti_hesabla(12.5, 20, 7.5)
# print(umumi)
#
# Nəticə:
#
# 40.0
#
# Məqsəd:
# print() və return arasındakı fərqi düzgün istifadə etmək.


# Kodunu burada yaz:




# ------------------------------------------------------------
# TAPŞIRIQ 6 — Default Parameter
# ------------------------------------------------------------
#
# "catdirilma_melumatini_goster" adlı function yarat.
#
# Function iki parameter qəbul etməlidir:
#
# seher
# catdirilma_novu
#
# "catdirilma_novu" parameter-inin default dəyəri:
#
# "Standart"
#
# olsun.
#
#
# Məsələn:
#
# catdirilma_melumatini_goster("Bakı")
#
# Nəticə:
#
# Şəhər: Bakı
# Çatdırılma: Standart
#
#
# Amma:
#
# catdirilma_melumatini_goster("Gəncə", "Express")
#
# Nəticə:
#
# Şəhər: Gəncə
# Çatdırılma: Express
#
#
# Function-u həm default parameter ilə,
# həm də öz göndərdiyin argument ilə yoxla.


# Kodunu burada yaz:




# ------------------------------------------------------------
# TAPŞIRIQ 7 — Məhsulun olub-olmadığını tap
# ------------------------------------------------------------
#
# Aşağıda məhsullar haqqında məlumat verilib.
#
# "mehsulu_tap" adlı function yarat.
#
# Function bir "ad" parameter-i qəbul etməlidir.
#
# Əgər həmin adda məhsul varsa:
# məhsulun dictionary-sini return et.
#
# Əgər məhsul yoxdursa:
# None return et.
#
#
# Məsələn:
#
# netice = mehsulu_tap("Monitor")
# print(netice)
#
# Nəticə:
#
# {'ad': 'Monitor', 'qiymet': 350, 'stok': 7}
#
#
# mehsulu_tap("Printer")
#
# nəticəsi isə None olmalıdır.
#
#
# TIP:
# for loop ilə məhsulları yoxla.
# Məhsulun "ad" dəyərini göndərilən parameter ilə müqayisə et.


mehsullar = [
    {
        "ad": "Laptop",
        "qiymet": 1800,
        "stok": 4
    },
    {
        "ad": "Monitor",
        "qiymet": 350,
        "stok": 7
    },
    {
        "ad": "Klaviatura",
        "qiymet": 80,
        "stok": 0
    },
    {
        "ad": "Mouse",
        "qiymet": 45,
        "stok": 12
    },
    {
        "ad": "Qulaqlıq",
        "qiymet": 120,
        "stok": 3
    }
]


# Kodunu burada yaz:




# ============================================================
# FINAL TAPŞIRIQ — Mini online mağaza sistemi
# ============================================================
#
# Yuxarıdakı "mehsullar" list-indən istifadə et.
#
# Aşağıdakı 3 function-u yarat.
#
#
# ------------------------------------------------------------
# 1. stokda_olanlari_goster()
# ------------------------------------------------------------
#
# Stok sayı 0-dan böyük olan bütün məhsulların adlarını
# və stok saylarını ekrana çıxarsın.
#
# Məsələn nəticənin formatı belə ola bilər:
#
# Laptop - 4 ədəd
# Monitor - 7 ədəd
# Mouse - 12 ədəd
#
# Stoku 0 olan məhsul göstərilməməlidir.
#
#
# TIP:
# for loop və if istifadə et.




# ------------------------------------------------------------
# 2. limitden_ucuz_mehsullar(limit)
# ------------------------------------------------------------
#
# Function bir "limit" parameter-i qəbul etsin.
#
# Qiyməti həmin limitdən aşağı olan məhsulların
# adlarını və qiymətlərini ekrana çıxarsın.
#
# Məsələn:
#
# limitden_ucuz_mehsullar(100)
#
# nəticəsində 100 AZN-dən ucuz məhsullar göstərilməlidir.
#
#
# TIP:
#
# if mehsul["qiymet"] < limit:
#     ...




# ------------------------------------------------------------
# 3. stok_sayini_hesabla()
# ------------------------------------------------------------
#
# Bütün məhsulların ümumi stok sayını hesablayan
# function yarat.
#
# Function nəticəni return etməlidir.
#
#
# Məsələn:
#
# umumi_stok = stok_sayini_hesabla()
# print(umumi_stok)
#
#
# TIP:
#
# umumi_stok = 0
#
# for loop daxilində hər məhsulun "stok" dəyərini
# umumi_stok variable-na əlavə et.




# ------------------------------------------------------------
# YOXLAMA
# ------------------------------------------------------------
#
# Function-larını aşağıdakı çağırışlarla yoxla:
#
#
# stokda_olanlari_goster()
#
# print("--------------------")
#
# limitden_ucuz_mehsullar(150)
#
# print("--------------------")
#
# umumi_stok = stok_sayini_hesabla()
# print(f"Ümumi stok: {umumi_stok}")
#
#
#
# ============================================================
# MƏQSƏD
# ============================================================
#
# Bu homework-da indiyə qədər keçdiyimiz mövzuları
# birlikdə istifadə etmək:
#
# - Sets
# - Lists
# - Dictionaries
# - Loops
# - Conditional Statements
# - Functions
# - Parameters və Arguments
# - Default Parameters
# - return
#
#
# Kodunu burada yaz:
