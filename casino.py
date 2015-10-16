stevilo = "22"
print("To je igra Ugani skrito stevilko!")
zadetek = raw_input("Stevilka je manjsa od 30 in vecja od 15! ")

loop_condition = True

while loop_condition:
    if stevilo == zadetek:
        print("Cestitamo! Uganili ste skrito stevilo!")
        loop_condition = False
    else:
        zadetek = raw_input("Poskusi ponovno!")
        loop_condition = True
