
for i in range(1, 201):
    print "LICZBA: " + str(i)
    dana = 0
    kandydat = i
    if str(kandydat) == str(kandydat)[::-1]:
        print ("Liczba " + str(i) + " jest juz palindromem i nie trzeba sprawdzac hipotezy")
    else:
        j = 0
        while (dana != kandydat and j < 20):
            print "KANDYDAT: " + str(kandydat)
            tymczasowy = str(kandydat)[::-1]
            tymczasowy = tymczasowy.lstrip("0")
            dana = kandydat + int(tymczasowy)
            print "dana: " + str(dana)
            tymczasowy2 = str(dana)[::-1]
            tymczasowy2 = tymczasowy2.lstrip("0")
            kandydat = int(tymczasowy2)
            if (dana == kandydat):
                print ("Dla liczby " + str(i) + " sprawdzono hipoteze i wyliczono PALIDROM " + str(dana))
                break
            j += 1
        else:
            print "liczba: " + str(i) + " chyba NIE jest palindromem, bo po " + str(j) + " iteracjach nie znaleziono"

