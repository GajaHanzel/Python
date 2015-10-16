stevilo = raw_input("Vpisi celo stevilko od 1-100 ")
if stevilo.isdigit():
    stevilo = int(stevilo)
    if stevilo < 1 or stevilo > 100:
        print"Rekel sem med 1 in 100!"
    else:
        for x in range(1, int(stevilo)):

            if x % 3 == 0 and x % 5 == 0:
                print"fizzbuzz"

            elif x % 5 == 0:
                print"buzz"

            elif x % 3 == 0:
                print"fizz"

            else:
                print x

else:
    print"To ni stevilka!"