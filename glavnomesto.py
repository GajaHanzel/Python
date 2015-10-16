import random

glavna_mesta = {
    "nizozemska": "amsterdam",
    "slovenija": "ljubljana",
    "srbija": "beograd",
    "nemcija": "berlin",
    "svica": "bern",
    "francija": "pariz",
}

def prestolnica(drzava):
    if drzava in glavna_mesta:
        return glavna_mesta[drzava]
    else:
        return False

def preveri_glavno_mesto(glavno_mesto, drzava):
    if glavno_mesto == prestolnica(drzava):
        return True
    else:
        return False




print random

tocke = 0

while True:
    drzava = random.sample(glavna_mesta, 1)[0]
    gl_mesto = raw_input("vnesi glavno mesto za drzavo %s ali prekini s stop " % drzava)
    if gl_mesto == "stop":
        break

    uganil = preveri_glavno_mesto(gl_mesto, drzava)
    if uganil == True:
        tocke += 1
    else:
        tocke -= 1


print "Bravo, imas %d tocko" % tocke

