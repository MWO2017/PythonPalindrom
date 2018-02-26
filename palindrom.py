
#for i in range (1, 201):
i = 199
dana = 0
kandydat = 199
if str(kandydat) == str(kandydat)[::-1]:
    print ("Liczba " + str(i) + " jest juz palindromem i nie trzeba sprawdzac hipotezy")
else:
 while (dana != kandydat):
     dana = kandydat + int(str(kandydat)[::-1])
     kandydat = int(str(dana)[::-1])
     if (dana == kandydat):
         print ("Dla liczby " + str(i) + " sprawdzono hipoteze i wyliczono PALIDROM " + str(dana))

