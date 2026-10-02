"""
TAPŞIRIQ:
"Restoran Menyu və Sifariş Sistemi" hazırlayın.

Məqsəd:
İndiyə qədər keçdiyimiz Python mövzularını bir proqram daxilində birlikdə istifadə etmək.

İstifadə etməli olduğunuz mövzular:

- Variables və Data Types
- Operators
- if / elif / else
- for və while
- Strings
- Lists
- Tuples
- Dictionaries
- Sets
- Functions
- input()
- Validation

Aşağıdakı restoran menyusu sizin üçün hazır verilib:

KATEQORIYALAR = (
    "Pizza",
    "Burger",
    "Salat",
    "İçki",
    "Desert"
)

menu = [
    {
        "ad": "Margherita Pizza",
        "kateqoriya": "Pizza",
        "qiymet": 12.50,
        "movcuddur": True
    },
    {
        "ad": "Pepperoni Pizza",
        "kateqoriya": "Pizza",
        "qiymet": 15.00,
        "movcuddur": True
    },
    {
        "ad": "Chicken Burger",
        "kateqoriya": "Burger",
        "qiymet": 9.50,
        "movcuddur": True
    },
    {
        "ad": "Cheeseburger",
        "kateqoriya": "Burger",
        "qiymet": 11.00,
        "movcuddur": False
    },
    {
        "ad": "Caesar Salat",
        "kateqoriya": "Salat",
        "qiymet": 8.50,
        "movcuddur": True
    },
    {
        "ad": "Cola",
        "kateqoriya": "İçki",
        "qiymet": 3.00,
        "movcuddur": True
    },
    {
        "ad": "Ayran",
        "kateqoriya": "İçki",
        "qiymet": 2.00,
        "movcuddur": True
    },
    {
        "ad": "Cheesecake",
        "kateqoriya": "Desert",
        "qiymet": 6.50,
        "movcuddur": True
    },
    {
        "ad": "Chocolate Cake",
        "kateqoriya": "Desert",
        "qiymet": 7.00,
        "movcuddur": False
    }
]

Bu menyunu dəyişdirməyə ehtiyac yoxdur.
Tapşırıqları bu data üzərində yerinə yetirin.

Müştərinin sifarişlərini saxlamaq üçün boş list yaradın.

Məsələn:

sifaris = []

Sifarişə əlavə edilən hər məhsul dictionary olmalıdır.

Məsələn:

{
    "ad": "Margherita Pizza",
    "qiymet": 12.50,
    "miqdar": 2
}

Bu funksiyanı yaradın:

def menyunu_goster():

Funksiya menyudakı məhsulları göstərməlidir.

Yalnız "movcuddur" dəyəri True olan məhsulları göstərin.

Məhsulun:
- adı
- kateqoriyası
- qiyməti

ekranda göstərilməlidir.

Nümunə:

Margherita Pizza | Pizza | 12.50 AZN
Cola | İçki | 3.00 AZN

Bu funksiyanı yaradın:

def yemek_axtar():

İstifadəçidən məhsul adı və ya məhsul adının bir hissəsini alın.

Məsələn:

Axtarış: pizza

Əgər menyuda uyğun məhsullar varsa, onları göstərin.

Axtarış böyük/kiçik hərfə həssas olmamalıdır.

Məsələn:
"pizza"
"Pizza"
"PIZZA"

eyni nəticəni verməlidir.

İpucu:
.strip()
.lower()
in

Əgər uyğun məhsul yoxdursa:
"Məhsul tapılmadı."

mesajını göstərin.

Bu funksiyanı yaradın:

def sifaris_elave_et():

İstifadəçidən məhsulun adını istəyin.

Proqram:
1. Məhsulun menyuda olub-olmadığını yoxlamalıdır.
2. Məhsulun "movcuddur" dəyərinin True olub-olmadığını yoxlamalıdır.
3. Miqdarı soruşmalıdır.

Əgər məhsul menyuda var, amma "movcuddur" dəyəri False-dursa:
"Məhsul hazırda mövcud deyil."

mesajını göstərin.

Miqdar üçün validation yazın.

Miqdar:
- rəqəm olmalıdır
- 0-dan böyük olmalıdır

Yanlış məlumat daxil edilərsə proqram çökməməlidir.
Düzgün məlumat daxil edilənə qədər yenidən soruşmalıdır.

Məsələn:

Miqdar: abc
Yanlış miqdar.

Miqdar: -2
Yanlış miqdar.

Miqdar: 0
Yanlış miqdar.

Miqdar: 2

Məhsul sifarişə əlavə ediləndən sonra:
"Margherita Pizza sifarişə əlavə edildi."

kimi mesaj göstərin.

Bu funksiyanı yaradın:

def sifarisi_goster():

Əgər sifariş boşdursa:
"Sifariş boşdur."

mesajını göstərin.

Əks halda sifarişdəki bütün məhsulları göstərin.

Hər məhsul üçün:
- məhsul adı
- miqdar
- bir ədədin qiyməti
- həmin məhsulun ümumi qiyməti

göstərilməlidir.

Nümunə:

--- SİFARİŞ ---

Margherita Pizza
2 x 12.50 AZN = 25.00 AZN

Cola
2 x 3.00 AZN = 6.00 AZN

Bu funksiyanı yaradın:

def umumi_meblegi_hesabla():

Sifarişdəki bütün məhsulların qiymətini hesablayın.

İpucu:
qiymet * miqdar

Sonra bütün nəticələri bir variable'da toplayın.

Ümumi məbləğə əsasən endirim tətbiq edin.

Qaydalar:

50 AZN-dən aşağı:
Endirim yoxdur

50 - 99.99 AZN:
5% endirim

100 AZN və daha çox:
10% endirim

Nümunə:

Sifariş məbləği: 120.00 AZN
Endirim: 12.00 AZN
Yekun məbləğ: 108.00 AZN

Menyuda istifadə olunan unikal kateqoriyaları tapın.
Bunun üçün set istifadə edin.

Nümunə nəticə:
{"Pizza", "Burger", "İçki", "Desert"}

Proqram dayanmadan işləməli və istifadəçiyə aşağıdakı menu göstərilməlidir:

--- RESTORAN SİSTEMİ ---

1. Menyunu göstər
2. Yemək axtar
3. Sifariş əlavə et
4. Sifarişi göstər
5. Hesabı göstər
6. Çıxış

İstifadəçi seçim etdikdə uyğun function çağırılmalıdır.

Yanlış seçim edilərsə:
"Yanlış seçim."

mesajını göstərin.

"6" seçildikdə proqram bağlanmalıdır.

İpucu:

while True:
    ...

    if secim == "1":
        ...

    elif secim == "2":
        ...

Restoran sifarişi üçün sadə "masa nömrəsi" sistemi əlavə edin.

Proqram başlayanda istifadəçidən masa nömrəsini istəyin.

Masa nömrəsi:
- rəqəm olmalıdır
- 1-20 arasında olmalıdır

Sifariş göstəriləndə masa nömrəsi də göstərilməlidir.

Nümunə:

Masa: 7

--- SİFARİŞ ---

Margherita Pizza
2 x 12.50 AZN = 25.00 AZN

Cola
2 x 3.00 AZN = 6.00 AZN

Ara məbləğ: 31.00 AZN
Endirim: 0.00 AZN
Yekun məbləğ: 31.00 AZN

TƏLƏBLƏR:

1. Bütün kod bir .py faylında olmalıdır.
2. Funksiyalardan istifadə edilməlidir.
3. Kod işləyərkən yanlış input proqramı çökdürməməlidir.
4. Variable və function adları aydın olmalıdır.
5. Kodda lazımsız təkrarlardan qaçmağa çalışın.
6. Hazır həlli internetdən və ya AI-dan kopyalamayın.
   Məqsəd keçdiyimiz mövzuları özünüz tətbiq etmək və məntiqi anlamaqdır.

Fayl adı:

phase_1_final.py

Uğurlar!
"""

KATEQORIYALAR = (
    "Pizza",
    "Burger",
    "Salat",
    "İçki",
    "Desert"
)

menu = [
    {
        "ad": "Margherita Pizza",
        "kateqoriya": "Pizza",
        "qiymet": 12.50,
        "movcuddur": True
    },
    {
        "ad": "Pepperoni Pizza",
        "kateqoriya": "Pizza",
        "qiymet": 15.00,
        "movcuddur": True
    },
    {
        "ad": "Chicken Burger",
        "kateqoriya": "Burger",
        "qiymet": 9.50,
        "movcuddur": True
    },
    {
        "ad": "Cheeseburger",
        "kateqoriya": "Burger",
        "qiymet": 11.00,
        "movcuddur": False
    },
    {
        "ad": "Caesar Salat",
        "kateqoriya": "Salat",
        "qiymet": 8.50,
        "movcuddur": True
    },
    {
        "ad": "Cola",
        "kateqoriya": "İçki",
        "qiymet": 3.00,
        "movcuddur": True
    },
    {
        "ad": "Ayran",
        "kateqoriya": "İçki",
        "qiymet": 2.00,
        "movcuddur": True
    },
    {
        "ad": "Cheesecake",
        "kateqoriya": "Desert",
        "qiymet": 6.50,
        "movcuddur": True
    },
    {
        "ad": "Chocolate Cake",
        "kateqoriya": "Desert",
        "qiymet": 7.00,
        "movcuddur": False
    }
]
