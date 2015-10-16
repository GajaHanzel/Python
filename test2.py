izdelki_cene = {
    "mleko": 2.25,
    "kruh": 1.44,
    "sok": 1.22,
    "jajca": 3,
    "salama": 1.44,
    "jogurt": 1.44
}

izbira = raw_input("Izberi izdelek: ")

if izbira in izdelki_cene.keys():
    cena = izdelki_cene[izbira]
    print "Cena izdelka je %s eur" % cena
else:
    print "Izdelka ni na zalogi"