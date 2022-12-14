print("Tere! Olen sinu uus sõber - Python!")
try:
    nimi = str(input("Mis sinu nimi on? "))
    if nimi.isalpha() == False :
        print("Kirjuta õige nimi")

    else:
        print(f"{nimi}, oi kui ilus nimi")
        imt = int(input(f"{nimi}! Kas leian Sinu keha indeksi? 0-ei, 1-jah => "))
        if imt == 1 :
                mass=float(input("Sinu kaal? - "))
                pikkus=int(input("Sinu pikkus? (Täisarv) - "))
                if mass<201 and pikkus<250 and mass>2 and pikkus>30:
                    index=round(mass/(0.01 * pikkus)**2, 1)
                    print(f"{nimi}! Sinu keha indeks on: {index}")
                    if index <16 :
                        print("Sinul on tervisele ohtlik alakaal!")
                    elif index>= 16 and index<19 :
                        print("Sinul on alakaal")
                    elif index>= 19 and index<25 :
                        print("Sinul on normaalkaal")
                    elif index>=25 and index<30 :
                        print("Sinul on ülekaal")
                    elif index>=30 and index<35 :
                        print("Sinul on rasvumine")
                    elif index>=35 and index<40 :
                        print("Sinul on tugev rasvumine")
                    elif index>40 :
                        print("Sinul on tervisele")
                else:
                 print("Palun kirjuta õige kaal ja mass!")
        else:
            print("Kahju! See on väga kasulik info!")
            print("")
            print("Kohtumiseni, " + nimi + "! Igavesti Sinu, Python!")
except:
    print("Viga!")