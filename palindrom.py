debug=1

for i in range(1, 201):
    print "LICZBA: " + str(i)
    dana = 0
    kandydat = i
    if str(kandydat) == str(kandydat)[::-1]:
        print ("Liczba " + str(i) + " jest _JUZ_ palindromem i nie trzeba sprawdzac hipotezy")
    else:
        j = 0
        #wyliczamy nowego kandydata wg teorii
        tymczasowy = int((str(kandydat)[::-1]).strip("0"))
        nowy_kandydat=kandydat + tymczasowy
        odwrocony_nowy_kandydat=False
        #if debug == 1: print str(j+1)+". nowy kandydat: "+str(nowy_kandydat)
        
        while (nowy_kandydat != odwrocony_nowy_kandydat and j <30):
            if debug == 1: print str(j+1)+". nowy kandydat: "+str(nowy_kandydat)
            odwrocony_nowy_kandydat=int((str(nowy_kandydat)[::-1]).lstrip("0"))
            if debug == 1: print "odwrocony nowy kandydat: "+str(odwrocony_nowy_kandydat)
            if nowy_kandydat==odwrocony_nowy_kandydat:
                print ("Dla liczby " + str(i) + " sprawdzono hipoteze i wyliczono PALIDROM " + str(nowy_kandydat))
                break
            else:
                nowy_kandydat=nowy_kandydat+odwrocony_nowy_kandydat
            j+=1
        else:
            print "liczba: " + str(i) + " chyba NIE jest palindromem, bo po " + str(j) + " iteracjach nie znaleziono"