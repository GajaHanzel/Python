DNA = "ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAATTACAGACCTGAA"

osumljenec_Ziga = "moski, belec, oranznolas, rjavook, okrogel obraz"
osumljenec_Matej = "moski, belec, crnolas, modrook, ovalen obraz"
osumljenec_Miha = "moski, belec, rjavolas, zelenook, kvadraten obraz"

if DNA.find("TGCAGGAACTTC") != -1:
    #print("moski")
    Spol = "moski"
else:
    #print("zenska")
    Spol = "zenska"

if DNA.find("AAAACCTCA") != -1:
    #print("belec")
    Rasa = "belec"

elif DNA.find("CGACTACAG") != -1:
    #print("crnec")
    Rasa = "crnec"

elif DNA.find("CGCGGGCCG") != -1:
    #print("azijec")
    Rasa = "azijec"

if DNA.find("CCAGCAATCGC") != -1:
    #print("crnolas")
    BarvaLas = "crnolas"

elif DNA.find("GCCAGTGCCG") != -1:
    #print("rjavolas")
    BarvaLas = "rjavolas"

elif DNA.find("TTAGCTATCGC") != -1:
    #print("oranznolas")
    BarvaLas = "oranznolas"

if DNA.find("TTGTGGTGGC") != -1:
    #print("modrook")
    BarvaOci = "modrook"

elif DNA.find("GGGAGGTGGC") != -1:
    #print("zelenook")
    BarvaOci = "zelenook"

elif DNA.find("AAGTAGTGAC") != -1:
    #print("rjavook")
    BarvaOci = "rjavook"

if DNA.find("GCCACGG") != -1:
    #print("kvadraten obraz")
    OblikaObraza = "kvadraten obraz"

elif DNA.find("ACCACAA") != -1:
    #print("okrogel obraz")
    OblikaObraza = "okrogel obraz"

elif DNA.find("AGGCCTCA") != -1:
    #print("ovalen obraz")
    OblikaObraza = "ovalen obraz"


krivec = Spol + ", "+ Rasa + ", "+ BarvaLas + ", "+ BarvaOci + ", " + OblikaObraza
print(krivec)

if krivec == osumljenec_Ziga:
    print("Sladoled je pojedel Ziga!")

elif krivec == osumljenec_Miha:
    print("Sladoled je pojedel Miha!")

elif krivec == osumljenec_Matej:
    print("Sladoled je pojedel Matej!")




