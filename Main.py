# :::::::::::::::::::::::::::::Variablen:::::::::::::::::::::::::::::

# All:

ff5 = {"Deutsch":0,"Englisch":0,"Latein":0,"Französisch":0,"Spanisch":0,"Mathematik":0,"Biologie":0,"Chemie":0,"Physik":0,"NaWi":0,"Informatik":0,"ITG":0,"Erdkunde":0,"Geschichte":0,"Sozialkunde":0,"Sport":0,"Religion":0,"Philosophie":0,"Bildende Kunst":0,"Darstellendes Spiel":0,"Musik":0}
ff6 = {"Deutsch":0,"Englisch":0,"Latein":0,"Französisch":0,"Spanisch":0,"Mathematik":0,"Biologie":0,"Chemie":0,"Physik":0,"NaWi":0,"Informatik":0,"ITG":0,"Erdkunde":0,"Geschichte":0,"Sozialkunde":0,"Sport":0,"Religion":0,"Philosophie":0,"Bildende Kunst":0,"Darstellendes Spiel":0,"Musik":0}
ff7 = {"Deutsch":0,"Englisch":0,"Latein":0,"Französisch":0,"Spanisch":0,"Mathematik":0,"Biologie":0,"Chemie":0,"Physik":0,"NaWi":0,"Informatik":0,"ITG":0,"Erdkunde":0,"Geschichte":0,"Sozialkunde":0,"Sport":0,"Religion":0,"Philosophie":0,"Bildende Kunst":0,"Darstellendes Spiel":0,"Musik":0}
ff8 = {"Deutsch":0,"Englisch":0,"Latein":0,"Französisch":0,"Spanisch":0,"Mathematik":0,"Biologie":0,"Chemie":0,"Physik":0,"NaWi":0,"Informatik":0,"ITG":0,"Erdkunde":0,"Geschichte":0,"Sozialkunde":0,"Sport":0,"Religion":0,"Philosophie":0,"Bildende Kunst":0,"Darstellendes Spiel":0,"Musik":0}
ff9 = {"Deutsch":0,"Englisch":0,"Latein":0,"Französisch":0,"Spanisch":0,"Mathematik":0,"Biologie":0,"Chemie":0,"Physik":0,"NaWi":0,"Informatik":0,"ITG":0,"Erdkunde":0,"Geschichte":0,"Sozialkunde":0,"Sport":0,"Religion":0,"Philosophie":0,"Bildende Kunst":0,"Darstellendes Spiel":0,"Musik":0}



for i in range(5,10):
    if i == 5:
        print("5. Stufe: \n")
        for k in ff5:
            ein = int(input("Anzahl der "+str(k)+" Stunden der "+str(i)+" Stufe: "))
            ff5[k] = ein
    elif i == 6:
        print("\n 6. Stufe: \n")
        for k in ff6:
            ein = int(input("Anzahl der "+str(k)+" Stunden der "+str(i)+" Stufe: "))
            ff6[k] = ein
    elif i == 7:
        print("\n 7. Stufe: \n")
        for k in ff7:
            ein = int(input("Anzahl der "+str(k)+" Stunden der "+str(i)+" Stufe: "))
            ff7[k] = ein
    elif i == 8:
        print("\n 8. Stufe: \n")
        for k in ff8:
            ein = int(input("Anzahl der "+str(k)+" Stunden der "+str(i)+" Stufe: "))
            ff8[k] = ein
    else:
        print("\n 9. Stufe: \n")
        for k in ff9:
            ein = int(input("Anzahl der "+str(k)+" Stunden der "+str(i)+" Stufe: "))
            ff9[k] = ein

stufe = []
# Tage:
mo = []
di = []
mi = []
do = []
fr = []
    
# Klassen:
a = []
b = []
c = []
d = []

schule = [mo,di,mi,do,fr]
stufe.append(a)
mo.append(stufe)

for i in range(10):
    a.append("test")

print(schule[0][0][0][:-1])

# :::::::::::::::::::::::::::UNTERPROGRAMME::::::::::::::::::::::::

