print("""********************************************
Tələbə idarə etmə Proqramına xoş gəldiniz!
Aşağıdakı əməliyyatlardan birini sıra nömrəsinə uyğun seçin.
Əməliyyatlar:

1. Yeni tələbə əlavə edilməsi
2. Tələbə koduna görə tələbə məlumatlarının silinməsi
3. Tələbə koduna görə tələbə məlumatlarının dəyişdirilməsi
4. Tələbə adına görə tələbə məlumatlarının göstərilməsi
5. Bütün tələbə məlumatlarının göstərilməsi
Qeyd: Proqramdan çıxmaq üçün "6" -ya basın.
""")
telebe = []
while True:
  operation = int(input("Əməliyyatı seçin: "))
  if (operation>0 and operation<7 ):
    if (operation == 6):
        print("Proqramdandan istifadə etdiyiniz üçün təşəkkür edirik!")
        break
    #1. Yeni tələbə əlavə edilməsi
    elif (operation == 1):
        print("""
        Tələbə üçün daxil ediləcək məlumatlar:
        -Tələbə kodu (3rəqəmli bir ədəd daxil edin!)
        -Tələbə adı
        -Tələbə soyadı
        -Tələbə email adresi(example@gmail.com)
        -Tələbə telefon nömrəsi(505213141)""")
        telebeSayi = 0
        while telebeSayi<10:
            kod = input("Tələbə kodunuzu daxil edin: ")
            while True:
                if len(kod)==3 and kod.isdigit():
                    break
                else:
                    kod = input("Tələbə kodunuzu daxil edin: ")
            ad = input("Adınızı daxil edin: ")
            soyad = input("Soyadınızı daxil edin: ")
            while True:
                email = input("E-mailinizi daxil edin: ")
                if ("@" in email):
                    break
                else:
                    print(email)
            telefon = input("Telefon nömrənizi daxil edin(505112131): ")
            while True:
                if len(telefon)==9 and telefon.isdigit():
                    telefon="+994" +telefon
                    break
                else:
                    telefon = input("Telefon nömrənizi düzgün daxil edin(505112131): ")
            telebeSayi+=1
            telebe+=[[kod, ad,soyad,email,telefon]]
            cixis = input("Əməliyyatdan çıxmaq üçün 'q' -ə basın, əks halda istənilən düyməyə basın.")
            if cixis=="q":
                break
    #2. Tələbə koduna görə tələbə məlumatlarının silinməsi
    elif (operation == 2 and len(telebe)!=0):
        tapKod = input("Silmək istədiyiniz tələbə məlumatlarına uyğun tələbə kodu daxil edin: ")
        print(telebe)
        for i in range(len(telebe)):
            telebeKod = telebe[i][0]
            if telebeKod==tapKod:
                telebe.pop(i)
        print(telebe)
    #3. Tələbə koduna görə tələbə məlumatlarının dəyişdirilməsi
    elif (operation == 3 and len(telebe)!=0):
        print(telebe)
        tapKod = input("Məlumatlarını dəyişmək istədiyiniz tələbənin kodunu daxil edin: ")
        for i in range(len(telebe)):
            telebeKod = telebe[i][0]
            if telebeKod==tapKod:
                    deyisenAd = input("Adınızı daxil edin: ")
                    deyisenSoyad = input("Soyadınızı daxil edin: ")
                    while True:
                        deyisenEmail = input("Emailinizi daxil edin: ")
                        if ("@" in deyisenEmail):
                            break
                        else:
                            print(deyisenEmail)
                    while True:
                        deyisenTelefon = input("Telefon nömrənizi daxil edin(505112131): ")
                        if len(deyisenTelefon)==9 and deyisenTelefon.isdigit():
                            deyisenTelefon="+994" + deyisenTelefon
                            break
                        else:
                            print(deyisenTelefon)
                    telebe[i][1] = deyisenAd
                    telebe[i][2] = deyisenSoyad
                    telebe[i][3] = deyisenEmail
                    telebe[i][4] = deyisenTelefon
        print(telebe)
    #4. Tələbə adına görə tələbə məlumatlarının göstərilməsi
    elif (operation==4 and len(telebe)!=0):
        tapilanAd = input("Tələbə adınızı daxil edin: ")
        for i in range(len(telebe)):
            telebeMelumatiAd = telebe[i][1]
            if telebeMelumatiAd==tapilanAd:
                x = " "
                for j in range(5):
                    x += telebe[i][j] + ", "
                print(x)
    #5. Bütün tələbə məlumatlarının göstərilməsi
    elif (operation==5 and len(telebe)!=0):
        telebeList = " "
        for a in range(len(telebe)):
            for b in range(len(telebe[a])):
                telebeList+=telebe[a][b]+ ", "
            print(telebeList)
            telebeList = " "
    else:
        print("Göstəriləcək tələbə məlumatı yoxdur, yeni tələbə daxil edin!")
  else:
      print("Düzgün rəqəm daxil edin!")
