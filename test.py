izdelki = ["mleko", "kruh", "jajca", "sok", "salama", "jogurt"]
cene_eur = [1, 2, 3, 1.44, 3.34, 1.05]

izbira = raw_input("Kateri izdelek si zelite? ")
if izbira in izdelki:
    indeks_izdelka = izdelki.index(izbira)
    cena_izdelka = cene_eur[index_izdelka]
    print "cena izdelka je %s eur" % (cena_izdelka)

else:
    print "izdelka ni na zalogi"


