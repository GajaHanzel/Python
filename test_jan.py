stevilo = "22"


zadetek = raw_input("Ugani skrito stevilko! Stevilka je manjsa od 30 in vecja od 15! ")

loop_condition = True

while loop_condition:
    if stevilo == zadetek:
        print("Cestitamo! Uganili ste skrito stevilo!")
        loop_condition = False
    elif stevilo < zadetek:
       zadetek = raw_input("Poskusi ponovno! Vneseno stevilo je premajhno")
    else:
        zadetek = raw_input("Poskusi ponovno! Vneseno stevilo je preveliko")




