#yeni telebe elave edilmesi
telebe = []
telebeSayi = 0
while telebeSayi<10:
    kod = input("Telebe kodunuzu daxil edin: ")
    while True:
        if len(kod)==3 and kod.isdigit():
            break
        else:
            print(kod)
    ad = input("Adinizi daxil edin: ")
                    #name surname
            if name.isdigit():
                print(ad)
            elif surname.isdigit():
               print(soyad)
            else:
                print("ad:" +name+ " "+"soyad :" +surname)
    soyad = input("Soyadinizi daxil edin: ")
    while True:
        email = input("Emailinizi daxil edin: ")
        if ("@" in email):
            break
        else:
            print(email)
    telefon = input("Telefon nomrenizi daxil edin: ")
    while True:
        if len(telefon)==9 and telefon.isdigit():
            telefon="+994" +telefon
            break
        else:
            print(telefon)
    telebeSayi+=1
    telebe+=[[kod, ad,soyad,email,telefon]]
    cixis = input("cixmaq isteyirsense q clickle ")
    if cixis=="q":
        break

#butun telebe melumatlarinin gosterilmesi
#print (telebe)

#telebe adina gore telebe melumatinin gosterilmesi
tapilanAd = input("Tapilan adinizi daxil edin: ")
for i in range(len(telebe)):
    telebeMelumati = telebe[i][1]
    if telebeMelumati==tapilanAd:
        for j in range(4):
            print(telebe[i][j])

"""#telebe melumatlari

telebeList = " "
for a in range(len(telebe)):
    for b in range(len(telebe[a])):
        telebeList+=telebe[a][b]+ "     "
    print(telebeList)
    telebeList = " "
    """

"""# Koda gore Silinme
tapKod = input("Tapilan kod daxil edin: ")
print(telebe)
for i in range(len(telebe)):
    telebeKod = telebe[i][0]
    if telebeKod==tapKod:
        telebe.pop(i)
print(telebe) """

# Telebe melumatarinin deyisdirilmesi
print(telebe)
tapKod = input("Tapilan kod daxil edin: ")
for i in range(len(telebe)):
    telebeKod = telebe[i][0]
    if telebeKod==tapKod:
            deyisenAd = input("Adinizi daxil edin: ")
            deyisenSoyad = input("Soyadinizi daxil edin: ")
            while True:
                deyisenEmail = input("Emailinizi daxil edin: ")
                if ("@" in email):
                    break
                else:
                    print(email)
            deyisenTelefon = input("Telefon nomrenizi daxil edin: ")
            while True:
                if telefon.isdigit():
                    telefon="+994" +telefon
                    break
                else:
                    telefon = input("Telefon nomrenizi daxil edin: ")
            telebe[i][1] = deyisenAd
            telebe[i][2] = deyisenSoyad
            telebe[i][3] = deyisenEmail
            telebe[i][4] = deyisenTelefon
print(telebe)
