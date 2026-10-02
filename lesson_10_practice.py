# ==========================================
# Tələbə İdarəetmə Sistemi
# Lesson 10 - Python əsasları üzrə praktika
# ==========================================


telebeler = []
telebe_adlari = set()

FENNLER = ("Python", "Git", "Məntiq")


# ------------------------------------------
# Balı istifadəçidən almaq və yoxlamaq
# ------------------------------------------

def bal_al(fenn):
    bal = input(f"{fenn} balını daxil et: ").strip()

    while not bal.isdigit() or int(bal) < 0 or int(bal) > 100:
        print("Bal 0-100 arasında olmalıdır.")
        bal = input(f"{fenn} balını yenidən daxil et: ").strip()

    return int(bal)


# ------------------------------------------
# Orta balı hesablamaq
# ------------------------------------------

def orta_bal_hesabla(ballar):
    cem = 0

    for bal in ballar:
        cem += bal

    return cem / len(ballar)


# ------------------------------------------
# Tələbənin statusunu müəyyən etmək
# ------------------------------------------

def status_tap(orta_bal):
    if orta_bal >= 90:
        return "Əla"

    elif orta_bal >= 70:
        return "Yaxşı"

    elif orta_bal >= 51:
        return "Keçdi"

    else:
        return "Kəsildi"


# ------------------------------------------
# Yeni tələbə əlavə etmək
# ------------------------------------------

def telebe_elave_et():
    print("\n--- Yeni tələbə ---")

    ad = input("Tələbənin adını daxil et: ").strip().title()

    # Eyni adlı tələbənin yenidən əlavə olunmasının qarşısını alırıq
    if ad in telebe_adlari:
        print("Bu adlı tələbə artıq mövcuddur.")
        return

    # Yaş
    yas = input("Tələbənin yaşını daxil et: ").strip()

    while not yas.isdigit():
        print("Yaş rəqəm olmalıdır.")
        yas = input("Yaşı yenidən daxil et: ").strip()

    yas = int(yas)

    # Ballar
    ballar = []

    for fenn in FENNLER:
        bal = bal_al(fenn)
        ballar.append(bal)

    # Tələbənin məlumatlarını dictionary-də saxlayırıq
    telebe = {
        "ad": ad,
        "yas": yas,
        "ballar": ballar
    }

    # Tələbəni list-ə əlavə edirik
    telebeler.append(telebe)

    # Adı set-ə əlavə edirik
    telebe_adlari.add(ad)

    print(f"\n{ad} uğurla əlavə edildi.")


# ------------------------------------------
# Bütün tələbələri göstərmək
# ------------------------------------------

def telebeleri_goster():
    if len(telebeler) == 0:
        print("\nSistemdə tələbə yoxdur.")
        return

    print("\n--- Tələbələr ---")

    for telebe in telebeler:

        orta_bal = orta_bal_hesabla(telebe["ballar"])
        status = status_tap(orta_bal)

        print("\n--------------------")
        print(f"Ad: {telebe['ad']}")
        print(f"Yaş: {telebe['yas']}")
        print(f"Ballar: {telebe['ballar']}")
        print(f"Orta bal: {orta_bal:.1f}")
        print(f"Status: {status}")

    print("--------------------")


# ------------------------------------------
# Tələbə axtarmaq
# ------------------------------------------

def telebe_axtar():
    if len(telebeler) == 0:
        print("\nSistemdə tələbə yoxdur.")
        return

    axtarilan_ad = input(
        "\nTələbənin adını daxil et: "
    ).strip().title()

    for telebe in telebeler:

        if telebe["ad"] == axtarilan_ad:

            orta_bal = orta_bal_hesabla(
                telebe["ballar"]
            )

            status = status_tap(orta_bal)

            print("\n--- Tələbə tapıldı ---")
            print(f"Ad: {telebe['ad']}")
            print(f"Yaş: {telebe['yas']}")
            print(f"Ballar: {telebe['ballar']}")
            print(f"Orta bal: {orta_bal:.1f}")
            print(f"Status: {status}")

            return

    print("\nTələbə tapılmadı.")


# ------------------------------------------
# Ən yüksək nəticəni göstərmək
# ------------------------------------------

def en_yuksek_netice():
    if len(telebeler) == 0:
        print("\nSistemdə tələbə yoxdur.")
        return

    # İlk tələbəni başlanğıc olaraq götürürük
    en_yaxsi_telebe = telebeler[0]

    en_yuksek_orta = orta_bal_hesabla(
        telebeler[0]["ballar"]
    )

    # Bütün tələbələri yoxlayırıq
    for telebe in telebeler:

        orta_bal = orta_bal_hesabla(
            telebe["ballar"]
        )

        if orta_bal > en_yuksek_orta:
            en_yuksek_orta = orta_bal
            en_yaxsi_telebe = telebe

    status = status_tap(en_yuksek_orta)

    print("\n--- Ən yüksək nəticə ---")
    print(f"Ad: {en_yaxsi_telebe['ad']}")
    print(f"Yaş: {en_yaxsi_telebe['yas']}")
    print(f"Ballar: {en_yaxsi_telebe['ballar']}")
    print(f"Orta bal: {en_yuksek_orta:.1f}")
    print(f"Status: {status}")


# ==========================================
# Əsas proqram
# ==========================================

while True:

    print("\n================================")
    print("     Tələbə İdarəetmə Sistemi")
    print("================================")

    print("1. Tələbə əlavə et")
    print("2. Tələbələri göstər")
    print("3. Tələbə axtar")
    print("4. Ən yüksək nəticəni göstər")
    print("5. Çıxış")

    secim = input("\nSeçimin: ").strip()

    if secim == "1":
        telebe_elave_et()

    elif secim == "2":
        telebeleri_goster()

    elif secim == "3":
        telebe_axtar()

    elif secim == "4":
        en_yuksek_netice()

    elif secim == "5":
        print("\nProqram bağlandı.")
        break

    else:
        print("\nYanlış seçim. 1-5 arasında seçim et.")
