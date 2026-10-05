"""
Dərs 5 — Ev tapşırığı
Mövzular:
- Conditional Statements və Loops — əlavə mövzular
- Strings ilə işləmə

Qaydalar:
- Bütün tapşırıqları bu faylın içində həll edin.
- Tapşırıq şərhlərini silməyin.
- Hər tapşırığın kodunu uyğun hissənin altına yazın.
- Proqramı fərqli input-larla test edin.
- Hazır kodu internetdən copy-paste etməyin.
- Məqsəd syntax-ı əzbərləmək yox, məntiqi özünüz qurmaqdır.
"""

# ============================================================
# TAPŞIRIQ 1 — Username yoxlanışı
# ============================================================

# İstifadəçidən username alın.
# Qaydalar:
# - əvvəl və sondakı boşluqlar silinsin
# - minimum 5 character olsun
# - username daxilində space olmasın
#
# Uyğundursa:
# Username accepted
#
# İPUCU:
# strip(), len(), " " in username, if / elif / else

# Kodunuzu burada yazın:


# ============================================================
# TAPŞIRIQ 2 — Mətn analizi
# ============================================================

# İstifadəçidən bir text alın.
# Çap edin:
# - ümumi uzunluq
# - ilk character
# - son character
# - böyük hərflərlə forması
# - kiçik hərflərlə forması
#
# İPUCU:
# len(), indexing, negative indexing, upper(), lower()

# Kodunuzu burada yazın:


# ============================================================
# TAPŞIRIQ 3 — Sözün tərsinə çevrilməsi
# ============================================================

# İstifadəçidən bir söz alın və tərsinə çevirib çap edin.
#
# Nümunə:
# Python -> nohtyP
#
# İPUCU:
# slicing və mənfi step istifadə edin.

# Kodunuzu burada yazın:


# ============================================================
# TAPŞIRIQ 4 — Character sayı
# ============================================================

# İstifadəçidən bir söz və ayrıca bir character alın.
# Həmin character-in söz daxilində neçə dəfə olduğunu hesablayın.
# Böyük və kiçik hərf fərqi nəzərə alınmasın.
#
# İPUCU:
# lower(), for loop, if
# count = 0

# Kodunuzu burada yazın:


# ============================================================
# TAPŞIRIQ 5 — Fayl növünü müəyyən edin
# ============================================================

# İstifadəçidən file name alın.
#
# .py   -> Python file
# .txt  -> Text file
# .jpg  -> Image file
# .png  -> Image file
# digər -> Unknown file type
#
# İPUCU:
# endswith(), if / elif / else, or

# Kodunuzu burada yazın:


# ============================================================
# TAPŞIRIQ 6 — Command sistemi
# ============================================================

# İstifadəçidən command alın.
#
# start   -> Starting...
# stop    -> Stopping...
# restart -> Restarting...
# status  -> System is running
# digər   -> Unknown command
#
# Böyük və kiçik hərf fərqi nəzərə alınmasın.
#
# İPUCU:
# input(...).strip().lower()
# match / case istifadə edin.

# Kodunuzu burada yazın:


# ============================================================
# TAPŞIRIQ 7 — Password yoxlanışı
# ============================================================

# İstifadəçidən password alın.
#
# Qaydalar:
# - minimum 8 character
# - space içərməməlidir
# - daxilində ən azı bir rəqəm olmalıdır
#
# Uyğundursa:
# Strong password
#
# Əks halda:
# Weak password
#
# QEYD:
# Hazır digit-checking method keçməmisiniz.
# Rəqəmləri String kimi yoxlaya bilərsiniz:
# "0", "1", ..., "9"
#
# İPUCU:
# has_digit = False
# for char in password:
#     ...
# Rəqəm tapsanız has_digit = True edin.

# Kodunuzu burada yazın:


# ============================================================
# TAPŞIRIQ 8 — Palindrome yoxlanışı
# ============================================================

# İstifadəçidən bir söz alın.
#
# Tərsinə oxunduqda da eynidirsə:
# Palindrome
#
# Əks halda:
# Not palindrome
#
# Böyük və kiçik hərf fərqi nəzərə alınmasın.
#
# İPUCU:
# lower(), slicing

# Kodunuzu burada yazın:


# ============================================================
# YEKUN TAPŞIRIQ — Sadə giriş sistemi
# ============================================================

# Bu məlumatlardan istifadə edin:
#
# correct_username = "admin"
# correct_password = "python123"
#
# İstifadəçiyə maksimum 3 cəhd verin.
#
# Hər cəhddə username və password daxil etsin.
#
# Username üçün:
# - əvvəl və sondakı boşluqları silin
# - böyük və kiçik hərf fərqi nəzərə alınmasın
#
# Əgər məlumatlar doğrudursa:
# Login successful
# çap edin və loop dayansın.
#
# Səhvdirsə:
# Invalid username or password
# çap edin.
#
# 3 cəhd bitdikdən sonra login alınmayıbsa:
# Too many failed attempts
# çap edin.
#
# İPUCU:
# for + range()
# if
# break
# loop else
# strip()
# lower()

# Kodunuzu burada yazın:
