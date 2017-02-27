# -*- coding: utf-8 -*-
class Vozilo:
    def __init__(self, znamka, model, prevozeni_km, datum_servisa):
        self.znamka = znamka
        self.model = model
        self.prevozeni_km = prevozeni_km
        self.datum_servisa = datum_servisa

    def dodaj_km(self, novi_km):
        self.prevozeni_km += novi_km

    def nov_datum_servisa(self, nov_datum):
        self.datum_servisa = nov_datum


def seznam_vozil(vozila):
    if vozila == []:
        print "Ni vnesenih vozil"
    else:
        for zap_st, vozilo in enumerate(vozila):
            print "%s) %s %s , %s prevozenih km. Zadnji servis: %s" % (zap_st+1, vozilo.znamka, vozilo.model, vozilo.prevozeni_km, vozilo.datum_servisa)


def ustvari_vozilo(znamka, model, prevozeni_km_str, datum_servisa, vozila):
    prevozeni_km_str = prevozeni_km_str.replace(",", ".")
    prevozeni_km = float(prevozeni_km_str)

    novo_vozilo = Vozilo(znamka, model, prevozeni_km, datum_servisa)
    vozila.append(novo_vozilo)
    return True


def dodaj_novo_vozilo(vozila):
    znamka = raw_input("Vnesite znamko vozila: ")
    model = raw_input("Vnesite model vozila: ")
    prevozeni_km_str = raw_input("Vnesite prevozene kilometre (samo stevilko): ")
    datum_servisa = raw_input("Vnesite datum zadnjega servisa (DD.MM.LLLL): ")

    izpolnjen_vnos = ustvari_vozilo(znamka, model, prevozeni_km_str, datum_servisa, vozila)

    if izpolnjen_vnos:
        print "Uspesno ste dodali novo vozilo %s %s!" % (znamka, model)
    else:
        print "Prosim preverite, ce ste vnesli vse podatke pravilno in poskusite znova."


def izberi_vozilo(vozila):
    print "Izberite zaporedno stevilko vozila, ki bi ga radi uredili."
    print ""
    seznam_vozil(vozila)
    print ""
    izbor = raw_input("Izberite zaporedno stevilko vozila: ")
    return vozila[int(izbor) - 1]


def dodaj_km(vozila):
    izbrano_vozilo = izberi_vozilo(vozila)

    print "Izbrano vozilo: %s %s s/z %s km." % (izbrano_vozilo.znamka, izbrano_vozilo.model, izbrano_vozilo.prevozeni_km)
    print ""
    novi_km_str = raw_input("Koliko km bi zeleli dodati(samo stevilo): ")
    print ""

    novi_km_str = novi_km_str.replace(",", ".")
    novi_km = float(novi_km_str)

    izbrano_vozilo.dodaj_km(novi_km)
    print "Prevozenih kilometrov za %s %s je sedaj: %s." % (izbrano_vozilo.znamka, izbrano_vozilo.model, izbrano_vozilo.prevozeni_km)


def spremeni_datum_servisa(vozila):
    izbrano_vozilo = izberi_vozilo(vozila)

    print "Izbrano vozilo: %s %s datum servisa: %s." % (izbrano_vozilo.znamka, izbrano_vozilo.model, izbrano_vozilo.datum_servisa)
    print ""
    nov_datum_servisa = raw_input("Vnsei nov datum servisa (DD.MM.LLLL): ")
    print ""
    izbrano_vozilo.nov_datum_servisa(nov_datum_servisa)
    print "Posodobljen datum servisa!"


def shrani(vozila):
    with open("vozila.txt", "w") as vozni_park:
        for vozilo in vozila:
            vozni_park.write("%s,%s,%s,%s\n" % (vozilo.znamka, vozilo.model, vozilo.prevozeni_km, vozilo.datum_servisa))


def main():
    print "Dobrodosli v voznem parku."

    vozila = []

    with open("vozila.txt", "r") as vozni_park:
        for vrstica in vozni_park:
            try:
                znamka, model, prevozeni_km_str, datum_servisa = vrstica.split(",")
                ustvari_vozilo(znamka, model, prevozeni_km_str, datum_servisa, vozila)
            except ValueError:
                continue

    while True:
        print ""
        print "Izberite eno od moznosti:"
        print "a) Seznam vseh vozil."
        print "b) Dodaj vozilo."
        print "c) Uredi prevozene kilometre."
        print "d) Uredi datum zadnjega servisa."
        print "e) Izhod."
        print ""

        izbor = raw_input("Izberite eno od moznosti? (a, b, c, d, e) ")
        print ""

        if izbor.lower() == "a":
            seznam_vozil(vozila)
        elif izbor.lower() == "b":
            dodaj_novo_vozilo(vozila)
        elif izbor.lower() == "c":
            dodaj_km(vozila)
        elif izbor.lower() == "d":
            spremeni_datum_servisa(vozila)
        elif izbor.lower() == "e":
            print "Hvala za uporabo Voznega parka."
            shrani(vozila)
            break
        else:
            print "Prosim preverite, ce ste izbrali pravilno in poskusite znova."

if __name__ == "__main__":
    main()