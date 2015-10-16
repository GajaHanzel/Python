listek = []
odgovor = raw_input("Tvoj nakupovalni listek je prazen. Zelis dodati kaksen izdelek? ")

while odgovor == "ja":
    izdelek_ena = raw_input("Vpisi izdelek: ")
    listek.append(izdelek_ena)
    odgovor = raw_input("Zelis dodati se kaksen izdelek? ")

print listek