"""
Dərs 4 — Ev tapşırığı
Mövzular: Conditional Statements və Loops

Qaydalar:
- Bütün tapşırıqları bu faylın içində həll edin.
- Tapşırıq şərhlərini silməyin.
- Hər tapşırığın kodunu uyğun hissənin altına yazın.
- Proqramı fərqli input-larla test edin.
- Hazır kodu internetdən copy-paste etməyin. Məqsəd məntiqi özünüz qurmaqdır.
- Ev tapşırığını tamamladıqdan sonra faylı GitHub repository-yə push edin.
"""

# ============================================================
# TAPŞIRIQ 1 — Yaş kateqoriyası
# ============================================================

# İstifadəçidən yaşını alın.
#
# Aşağıdakı qaydalara əsasən nəticəni çap edin:
#
# 0–12   -> Uşaq
# 13–17  -> Yeniyetmə
# 18–64  -> Yetkin
# 65+    -> Yaşlı
#
# Nümunə:
# Yaşınızı daxil edin: 16
# Yeniyetmə
#
# İPUCU:
# if, elif və else istifadə edin.
# Condition-ların sırasına diqqət edin.

# Kodunuzu burada yazın:


# ============================================================
# TAPŞIRIQ 2 — Rəqəmin analizi
# ============================================================

# İstifadəçidən bir integer alın.
#
# Proqram əvvəlcə rəqəmin:
# - Müsbət
# - Mənfi
# - Sıfır
#
# olduğunu müəyyən etsin.
#
# Əgər rəqəm sıfır deyilsə, əlavə olaraq:
# - Cüt
# - Tək
#
# olduğunu da çap etsin.
#
# Nümunə:
# Rəqəm daxil edin: -8
# Mənfi
# Cüt
#
# İPUCU:
# Müsbət / Mənfi / Sıfır üçün if / elif / else istifadə edə bilərsiniz.
# Cüt və Tək yoxlamaq üçün % operatorunu xatırlayın.
# number % 2 == 0

# Kodunuzu burada yazın:


# ============================================================
# TAPŞIRIQ 3 — for loop ilə rəqəmlər
# ============================================================

# 1-dən 50-yə qədər olan rəqəmlərin içindən yalnız
# 3-ə bölünən rəqəmləri çap edin.
#
# Gözlənilən nəticənin başlanğıcı:
# 3
# 6
# 9
# 12
# ...
#
# İPUCU:
# range() və for istifadə edin.
# Bir rəqəmin 3-ə tam bölünüb-bölünmədiyini % ilə yoxlaya bilərsiniz.

# Kodunuzu burada yazın:


# ============================================================
# TAPŞIRIQ 4 — Rəqəmlərin cəmi
# ============================================================

# İstifadəçidən müsbət integer alın.
#
# 1-dən həmin rəqəmə qədər bütün rəqəmlərin cəmini hesablayın.
#
# Nümunə:
# Rəqəm daxil edin: 5
# Cəm: 15
#
# Çünki:
# 1 + 2 + 3 + 4 + 5 = 15
#
# İPUCU:
# Əvvəl belə bir variable yarada bilərsiniz:
#
# total = 0
#
# Sonra for loop daxilində hər rəqəmi total-a əlavə edin.
#
# total = total + number
#
# və ya:
#
# total += number

# Kodunuzu burada yazın:


# ============================================================
# TAPŞIRIQ 5 — Geri sayım
# ============================================================

# İstifadəçidən müsbət integer alın.
#
# Həmin rəqəmdən 1-ə qədər geriyə sayın və sonda "Başla!" çap edin.
#
# Nümunə:
# Rəqəm daxil edin: 5
#
# 5
# 4
# 3
# 2
# 1
# Başla!
#
# İPUCU:
# range() üçün mənfi step istifadə edə bilərsiniz.
#
# range(start, stop, step)
#
# Burada step -1 ola bilər.

# Kodunuzu burada yazın:


# ============================================================
# TAPŞIRIQ 6 — Gizli rəqəm
# ============================================================

# secret_number adlı variable yaradın və dəyərini 7 edin.
#
# İstifadəçi doğru rəqəmi tapana qədər proqram ondan rəqəm istəsin.
#
# Əgər daxil edilən rəqəm secret_number-dan böyükdürsə:
# "Çox böyükdür"
#
# Əgər kiçikdirsə:
# "Çox kiçikdir"
#
# Əgər doğrudursa:
# "Doğrudur!"
#
# çap edin və loop dayansın.
#
# Nümunə:
#
# Rəqəmi tapın: 10
# Çox böyükdür
#
# Rəqəmi tapın: 4
# Çox kiçikdir
#
# Rəqəmi tapın: 7
# Doğrudur!
#
# İPUCU:
# while loop istifadə edin.
# Doğru cavab tapıldıqda break istifadə edə bilərsiniz.

# Kodunuzu burada yazın:


# ============================================================
# YEKUN TAPŞIRIQ — FizzBuzz
# ============================================================

# 1-dən 30-a qədər bütün rəqəmlərin üzərindən keçin.
#
# Əgər rəqəm həm 3-ə, həm də 5-ə bölünürsə:
# FizzBuzz
#
# Əgər yalnız 3-ə bölünürsə:
# Fizz
#
# Əgər yalnız 5-ə bölünürsə:
# Buzz
#
# Əks halda rəqəmin özünü çap edin.
#
# Nəticənin bir hissəsi belə görünəcək:
#
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
#
# İPUCU:
# for + if / elif / else istifadə edin.
#
# Ən vacib hissə:
# Həm 3-ə, həm 5-ə bölünmə condition-ını hansı sırada
# yoxlamağınız barədə düşünün.

# Kodunuzu burada yazın:
