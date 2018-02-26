
# for i in range (1, 201):
i = 199
dana = 0
kandydat = 196
if str(kandydat) == str(kandydat)[::-1]:
    print ("Liczba " + str(i) + " jest juz palindromem i nie trzeba sprawdzac hipotezy")
else:
    i=0
    while (dana != kandydat and i<300):
        dana = kandydat + int(str(kandydat)[::-1])
        print "dana: "+str(dana)
        kandydat = int(str(dana)[::-1])
        if (dana == kandydat):
            print ("Dla liczby " + str(i) + " sprawdzono hipoteze i wyliczono PALIDROM " + str(dana))
        i+=1

